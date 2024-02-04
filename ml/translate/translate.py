import translate_user_def as tud

input_text = input("Enter text to translate: ")
translate_lang = input("Enter language to translate to: ") 
input_arg = {
            'Text' : input_text, 
             'SourceLanguageCode' : 'EN',
             'TargetLanguageCode' : translate_lang
            }
#'Text' : input_text, 'Language' : translate_lang}
tud.validate_input_text(**input_arg)



