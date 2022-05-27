from django.contrib import admin
from plan import models


@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):
    pass


@admin.register(models.User_Plan)
class User_PlanAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Plan_Category)
class Plan_CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Hashtak)
class HashtakAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Plan_Hashtak)
class Plan_HashtakAdmin(admin.ModelAdmin):
    pass
