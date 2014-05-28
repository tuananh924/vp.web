from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic.base import TemplateView
from vpw.sitemaps import VoerSitemap, VoerCategoriesSitemap, VoerTypeSitemap, VoerLanguagesSitemap
from vpw.views import RecaptchaRegistrationView

admin.autodiscover()

sitemaps = {
    'static': VoerSitemap,
    'types': VoerTypeSitemap,
    'categories': VoerCategoriesSitemap,
    'languages': VoerLanguagesSitemap,
}

urlpatterns = patterns('',
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^language/', include('django.conf.urls.i18n')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^profile/(?P<pid>[0-9a-z]+)/delete$', 'vpw.views.delete_profile', name='delete_profile'),

    url(r'^$', 'vpw.views.home', name='home'),
    url(r'^m/(?P<mid>[0-9a-f]{8})(/(?P<version>\d+))?/?$', 'vpw.views.module_detail_old', name='module_detail_old'),
    url(r'^m/(?P<title>[0-9A-Za-z_\-]+)/(?P<mid>[0-9a-f]{8})(/(?P<version>\d+))?/?$', 'vpw.views.module_detail', name='module_detail'),
    url(r'^c/(?P<cid>[0-9a-f]{8})(/(?P<mid>[0-9a-f]{8}))?/?$', 'vpw.views.collection_detail_old', name='collection_detail_old'),
    url(r'^c/(?P<title>[0-9A-Za-z_\-]+)/(?P<cid>[0-9a-f]{8})(/(?P<mid>[0-9a-f]{8}))?/?$', 'vpw.views.collection_detail', name='collection_detail'),
    url(r'^browse/?$', 'vpw.views.browse', name='browse'),
    url(r'^signup/?$', 'vpw.views.signup', name='signup'),
    url(r'^profile/(?P<pid>[0-9a-z]+)/?$', 'vpw.views.view_profile', name='view_profile'),
    # unused link below
    url(r'^about-us/?$', 'vpw.views.aboutus', name='about-us'),

    ## User ###
    url(r'^user/register/?$', RecaptchaRegistrationView.as_view()),
    url(r'^user/', include('registration.backends.default.urls')),
    url(r'^user/authenticate$', 'vpw.views.vpw_authenticate', name='authenticate'),
    url(r'^user/dashboard/?$', 'vpw.views.user_dashboard', name='user_dashboard'),
    url(r'^user/logout$', 'vpw.views.vpw_logout', name='logout'),
    url(r'^user/create/module/?$', 'vpw.views.create_module', name='create_module'),
    url(r'^user/create/collection/?$', 'vpw.views.create_collection', name='create_collection'),
    url(r'^user/create/mass-modules/?$', 'vpw.views.create_mass_modules', name='create_mass_modules'),
    url(r'^user/create/mass-modules/import/?$', 'vpw.views.import_mass_modules', name='import_mass_modules'),
    url(r'^user/edit/profile/?$', 'vpw.views.edit_profile', name='edit_profile'),
    url(r'^user/reuse/m/(?P<mid>[0-9a-z]+)/(?P<version>\d+)/?$', 'vpw.views.user_module_reuse',
        name='user_module_reuse'),
    url(r'^user/m/(?P<mid>[0-9]+)/?$', 'vpw.views.user_module_detail', name='user_module_detail'),
    url(r'^user/c/(?P<cid>[0-9a-z]+)(/(?P<mid>[0-9a-z]+))?/?$', 'vpw.views.user_collection_detail',
        name='user_collection_detail'),
    url(r'^user/most-viewed/?$', 'vpw.views.mostViewedView', name='most-viewed'),
    url(r'^user/most-faved/?$', 'vpw.views.mostFavedView', name='most-faved'),
    url(r'^user/most-rated/?$', 'vpw.views.get_most_rated', name='most-rated'),
    url(r'^user/favorite/?$', 'vpw.views.get_favorite', name='get_favorite'),
    url(r'^user/unpublish/?$', 'vpw.views.get_unpublish', name='get_unpublish'),
    url(r'^user/unpublish/delete/?$', 'vpw.views.delete_unpublish', name='delete_unpublish'),
    url(r'^user/avatar/(?P<pid>[0-9a-z]+)/?$', 'vpw.views.get_avatar', name='get_avatar'),
    url(r'^user/edit/m/(?P<mid>[0-9a-z]+)/?$', 'vpw.views.user_module_edit', name="user_module_edit"),
    url(r'^user/edit/c/(?P<cid>[0-9a-z]+)/?$', 'vpw.views.user_collection_edit', name="user_collection_edit"),
    url(r'^user/publish/m/(?P<mid>[0-9a-z]+)/?$', 'vpw.views.user_publish_material', name="user_publish_material"),

    url(r'^admin/import-user/?$', 'vpw.views.admin_import_user', name='import-user'),
    url(r'^admin/settings/?$', 'vpw.views.admin_settings', name='settings'),
    url(r'^admin/featured-authors/?$', 'vpw.views.admin_featured_authors', name='featured-authors'),
    url(r'^admin/featured-materials/?$', 'vpw.views.admin_featured_materials', name='featured-materials'),

    url(r'^search/', 'vpw.views.search_result', name='search'),

    url(r'^pdf/(?P<mid>[0-9a-z]+)/(?P<version>\d+)/?$', 'vpw.views.get_pdf', name='get_pdf'),
    url(r'^attachment/m/(?P<fid>[0-9a-z]+)/?$', 'vpw.views.get_attachment', name='get_attachment'),
    url(r'^file/(?P<fid>[0-9a-z]+)/?$', 'vpw.views.get_content_file', name='get_content_file'),

    ## AJAX
    url(r'^ajax/browse$', 'vpw.views.ajax_browse', name='ajax_browse'),
    url(r'^ajax/add_favorite$', 'vpw.views.ajax_add_favorite', name='ajax_add_favorite'),
    url(r'^ajax/search_author$', 'vpw.views.ajax_search_author', name='ajax_search_author'),
    url(r'^ajax/search_module$', 'vpw.views.ajax_search_module', name='ajax_search_module'),
    url(r'^ajax/get-others$', 'vpw.views.ajax_get_others', name='ajax_get_others'),
    url(r'^ajax/get-similars', 'vpw.views.ajax_get_similars', name='ajax_get_similars'),
    url(r'^ajax/search-result$', 'vpw.views.ajax_search_result', name='ajax_search_result'),
    url(r'^ajax/user-rate$', 'vpw.views.ajax_user_rate', name='ajax_user_rate'),
    url(r'^ajax/remove-avatar$', 'vpw.views.ajax_user_remove_avatar', name='ajax_user_remove_avatar'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='frontend/robots.txt', content_type='text/plain')),

    url(r'^google9c25b243b9e3bacc\.html$', TemplateView.as_view(template_name='frontend/google9c25b243b9e3bacc.html')),
    url(r'^BingSiteAuth\.xml', TemplateView.as_view(template_name='frontend/BingSiteAuth.xml')),

    url(r'^content/', include('django.contrib.flatpages.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$',
                                    'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

handler500 = "vpw.views.server_error"
