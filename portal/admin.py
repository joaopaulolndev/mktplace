from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from django.contrib import admin

from portal.models import Category, Product, ProductAnswer, ProductQuestion


class CategoryAdmin(AjaxSelectAdmin):
    prepopulated_fields = {"slug": ('name', )}
    list_filter = ['hidden']
    list_display = ("id", "name", "parent", "hidden")
    form = make_ajax_form(Category, {
        'parent': 'categories'
    })


class ProductAdmin(AjaxSelectAdmin):
    prepopulated_fields = {"slug": ('name', )}
    list_filter = ['status']
    list_display = ("id", "name", "short_description", "status")

    # Primeiro parametro User eh o campo, segundo eh o lookup
    form = make_ajax_form(Product, {
        'user': 'user',
        # 'categories' : 'categories'
    })


class ProductAnswerInline(admin.StackedInline):
    model = ProductAnswer
    can_delete = False


class ProductQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'question', 'status')
    list_filter = ['status']
    inlines = (ProductAnswerInline,)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductQuestion, ProductQuestionAdmin)
