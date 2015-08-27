#!/usr/bin/env bash

# Run this script for the initial migration will use less RAM than running "python manage.py migrate",
# because the latter needs to figure out the order of all the dependencies which takes lots of memory.

# Note that: the initial 4 migrations will throw errors that can be safely ignored.
apps=("contenttypes 0002" \
 sites \
 "auth 0001" \
 "notifications" \
 "auth 0006" \
 "accountings 0001" \
 "admin 0001" \
 "entities 0001" \
 "announcements 0001" \
 "user_groups 0001" \
 "meta 0001" \
 "articles 0002" \
 "avatar 0001" \
 "base 0002" \
 "boxes 0001" \
 "invoices 0001" \
 "payments 0001" \
 "forms 0001" \
 "campaign_monitor 0001" \
 "captcha 0001" \
 "careers 0001" \
 "files 0001" \
 "case_studies 0001" \
 "categories 0001" \
 "pages 0001" \
 "committees 0001" \
 "contacts 0001" \
 "contacts 0002" \
 "contributions 0001" \
 "regions 0001" \
 "industries 0001" \
 "directories 0001" \
 "memberships 0001" \
 "emails 0001" \
 "events 0001" \
 "corporate_memberships 0002" \
 "dashboard 0001" \
 "directories 0002" \
 "discounts 0001" \
 "donations 0001" \
 "educations 0001" \
 "email_blocks 0001" \
 "robots 0001" \
 "event_logs 0001" \
 "events 0003" \
 "explorer 0002" \
 "explorer_extensions 0001" \
 "exports 0001" \
 "handler404 0001" \
 "help_files 0001" \
 "ics 0001" \
 "imports 0001" \
 "jobs 0001" \
 "locations 0001" \
 "make_payments 0001" \
 "memberships 0002" \
 "metrics 0001" \
 "navs 0001" \
 "news 0002" \
 "newsletters 0001" \
 "perms 0001" \
 "photos 0001" \
 "profiles 0002" \
 "recurring_payments 0001" \
 "redirects 0001" \
 "registration 0001" \
 "reports 0001" \
 "resumes 0001" \
 "search 0001" \
 "sessions 0001" \
 "site_settings 0001" \
 "social_auth 0001" \
 "speakers 0002" \
 "staff 0001" \
 "stories 0001" \
 "studygroups 0001" \
 "tagging 0001" \
 "tendenci_guide 0001" \
 "testimonials 0001" \
 "theme_editor 0001" \
 "versions 0001" \
 "videos 0002" \
 "wp_exporter 0001" \
 "wp_importer 0001" \
)

for app in "${apps[@]}"
do
    python -Wi manage.py migrate $app
done
