#Testitmonial

def testimonial_view(request):
    testimonials = Testimonial.objects.filter(is_approved=True)
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # is_approved stays False by default
            return redirect('testimonial')  # refresh page

    return render(request, 'yourapp/testimonial_page.html', {
        'form': form,
        'testimonials': testimonials,
    })