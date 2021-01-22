from django.contrib import admin

from apps.recipes import models


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'dimension')


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('description', )


class TagInline(admin.TabularInline):
    model = models.Recipe.tags.through
    extra = 0
    min_num = 1


class IngredientsInline(admin.TabularInline):
    model = models.RecipeIngredients
    extra = 0
    min_num = 1


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'cooking_time')
    exclude = ('tags', )
    inlines = (TagInline, IngredientsInline)


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
