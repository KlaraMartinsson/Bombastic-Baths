from django import forms
from .models import Rating, Review


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            "rating",
        ]

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating


class ReviewForm(forms.ModelForm):
    class Meta:
        """
        Form for writing product reviews
        """
        model = Review
        fields = [
            "content",
        ]
