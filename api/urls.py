from django.urls import path

from api import views

urlpatterns = [
    path('create/admin/', views.CreatePaydaAdmin.as_view()),
    path('create/agent/', views.CreatePaydaAgent.as_view()),
    path('create/sales/', views.CreateSalesManager.as_view()),
    path('create/client/', views.CreateWorkSheet.as_view()),
    path('create/worker/', views.CreateWorker.as_view()),
    path('create/activity/', views.CreateActivity.as_view()),
    path('create/tax/', views.CreateTax.as_view()),
    path('create/region/', views.CreateRegion.as_view()),
    path('create/payment/', views.CreatePayment.as_view()),
    path('create/message/', views.CreateMessage.as_view()),
    path('login/', views.APILoginView.as_view()),
    path('logout/', views.APILogoutView.as_view()),
    path('comment/', views.CreateComment.as_view()),
    path('dashboard/', views.dashboard),
    path('payments/', views.ListPayment.as_view()),
    path('agent/<int:pk>/', views.DetailAgent.as_view()),
    path('agent/block/<int:pk>/', views.BlockAgent.as_view()),
    path('clients/', views.ListClients.as_view()),
]
