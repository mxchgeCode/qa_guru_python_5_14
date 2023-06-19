from demoqa_tests.pages.registration_page import RegistrationPage


def test_form_filling_submitting(setup_browser):
    br = setup_browser
    registration_page = RegistrationPage(br)
    registration_page.open()
    registration_page.remove_banners()

    # WHEN
    registration_page.fill_first_name('Michael')
    registration_page.fill_last_name('Kors')
    registration_page.fill_email('Michael@Kors.com')
    registration_page.select_gender('Male')
    registration_page.fill_phone_number('8667095677')
    # registration_page.fill_date_of_birth('1959', 'August', '9')

    registration_page.fill_subject('English')
    registration_page.fill_subject('Accounting')
    registration_page.choose_hobbie('Music')
    registration_page.upload_picture('account.png')

    registration_page.fill_address('Rodriguez side, LA 93111')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Agra')
    registration_page.submit()

    # THEN
    # registration_page.should_registered_user_with(
    #     'Michael Kors',
    #     'Michael@Kors.com',
    #     'Male',
    #     '8667095677',
    #     #'9 August,1959',
    #     'English, Accounting',
    #     'Music',
    #     'account.png',
    #     'Rodriguez side, LA 93111',
    #     'Uttar Pradesh Agra',
    # )

    ...
