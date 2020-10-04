## Translating JS file strings to another language using Google Translator api 🔥 🔥 

#### What it do:

```
# en.js file
export default {
  name_error: "Name is required",
};

```

##### Output : 

```
# ur.js file
export default {
    name_error : "نام مطلوب ہے",
}
```

1. This python script reads key and values from 'en.js' .
2. Then converted the strings to desired language using google translator api <br>```result = Translation("en.js", "ur","en") ```

<br>

3. The converted strings write in to 'ur.js' file<br>```WritingTranslationToOtherFile("ur.js")```

<br>

> Too many requests to translator api will block your IP for one day (Google has a translate API that costs money to use so they want to stop free usage from other apis). Better to use in Jupyter Notebook or any or use VPN.

That's it. 😃😃

