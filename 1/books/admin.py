from django.contrib import admin
from .models import Book, Author, BorrowModel, Memeber


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_date",
                    "ISBN", "availability_status")
    list_filter = ("availability_status", )
    search_fields = ("title", "author", "publication_date", "ISBN")
 
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "contact_number", "is_active")
    list_filter = ("is_active", )
    search_fields = ("name", "email", "contact_number")
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "biography")
    list_filter = ("name", )
    search_fields = ("name",)
    
class BorrowModelAdmin(admin.ModelAdmin):
    list_display = ("member", "book", "borrow_date", "return_date")
    list_filter = ("borrow_date", "return_date")
    search_fields = ("member", "book", "borrow_date", "return_date")
    
        
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BorrowModel, BorrowModelAdmin)
admin.site.register(Memeber, MemberAdmin)
