from translate import Translator
translator= Translator(from_lang="English",to_lang="Hindi")

class Translator:
    def __init__(self, to_lang, from_lang='en', provider=None, secret_access_key=None, **kwargs):
        self.available_providers = list(PROVIDERS_CLASS.keys())
        self.from_lang = from_lang
        self.to_lang = to_lang
        if provider and provider not in self.available_providers:
            raise InvalidProviderError(
                'Provider class invalid. '
                'Please check providers list bellow: {!r}'.format(self.available_providers)
            )

        provider_class = PROVIDERS_CLASS.get(provider, DEFAULT_PROVIDER)

        self.provider = provider_class(
            from_lang=from_lang,
            to_lang=to_lang,
            secret_access_key=secret_access_key,
            **kwargs
        )

    def translate(self, text):
        if self.from_lang == self.to_lang:
            return text

        text_list = wrap(text, TRANSLATION_API_MAX_LENGHT, replace_whitespace=False)
        print(' '.join(self.provider.get_translation(text_wraped) for text_wraped in text_list))
        return ' '.join(self.provider.get_translation(text_wraped) for text_wraped in text_list)

def trans_lang():
    f=open('data_read1.txt')
    for i in f.readlines():
        print(translator.translate(i))
        print (i)
trans_lang()

    
