from django.contrib import admin

from apps.recipes import models


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'dimension')
    list_filter = ('name',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


class TagInline(admin.TabularInline):
    model = models.Recipe.tags.through
    extra = 0
    min_num = 1


class IngredientsInline(admin.TabularInline):
    model = models.Recipe.ingredients.through
    extra = 0
    min_num = 1


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'cooking_time')
    list_filter = ('name',)
    exclude = ('tags', )
    inlines = (TagInline, IngredientsInline)


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(models.Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
