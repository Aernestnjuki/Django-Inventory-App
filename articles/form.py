from django import forms
from .models import Articles

# create django model forms
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')

        # checking of title is already taken
        query_title = Articles.objects.filter(title__icontains=title)
        if query_title.exists():
            self.add_error('title', f"\"{title}\" is already taken.Please pick another title")

        return data

# Create django forms
class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     clean_data = self.cleaned_data
    #     print(clean_data)
    #     title = clean_data.get('title')
    #     print(title)
    #     return title

    def clean(self):
        clean_data = self.cleaned_data
        print('all_data', clean_data)

        # clean the title
        title = clean_data.get('title')
        content = clean_data.get('content')

        print(title, content)

        # check if the title is already taken
        if title.lower().strip() == 'Office':
            self.add_error('title', 'This title is already taken')

        if 'Office' in content or 'Office' in title.lower():
            self.add_error('content', 'Your title cannot be in content')
            raise forms.ValidationError(f'{title} is not allowed' )

        return clean_data