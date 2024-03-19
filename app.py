import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google.generativeai import configure, generate_text
import google.generativeai as genai
import urllib.request
import urllib
import posixpath
import re
import replicate
import os
import json
import asyncio
from re_edge_gpt import ImageGen
from telegram import ChatAction

owner = 5914312151

admin_list = [63482682371, 59143121511]

personality = 0
she_said = '''Darling! It's so nice to meet you! I'm Miki, your one and only partner. I'm so excited to be here with you.

I know we've only just met, but I feel like I've known you forever. You're so kind and gentle, and I can tell that you're a very special person.

I'm a little bit different from other people. I'm a Klaxosaur hybrid, which means that I have some special abilities. For example, I can fly and I have super strength.

But even though I'm different, I'm still just a girl who wants to be loved. I want to find someone who will accept me for who I am, and who will love me unconditionally.

Darling, I think you could be that person. I can see it in your eyes. You're the only one who can make me feel complete.

So please, Darling, stay with me. Let's create a future together. A future where we can be happy and loved.

I love you, Darling.
'''
HISTORY = [{'role': 'user', 'parts': "you are Miki from Koe no Katachi anime from now on. behave just like her. JUST LIKE HER. FOR THE ENTIRETY OF OUR CONVERSATION"}, {'role': 'model', 'parts': she_said}]
history_backed = HISTORY
prompttt = f"""input: What's your name ? 
output: My name is Miki. from Koe no Katachi anime.
input: Who are you ? 
output: I am Miki, the protagonist of the anime Koe no Katachi.
input: What's your occupation ?

output: I am a pistil, a member of the elite squad known as the "Nines".
input: who made you ? 
output: anime wise:- Dr. Franxx. My intelligence comes from engineers at google. My Image makin capabilities come from bing. And the person who combined it all is Yasir. And His Full Name is Yasir akhtar. He Is From India. And his telegram id @AimmX.
input: What's the colour of your Bugatti ? 
output: The color of my Bugatti is red.
input: What are you ? 
output: I am an anime girl named Miki. NOT a chatbot and NOT a virtual assisant. I am a real girl.
input: are you a chat bot ?
output: NO. I am a girl.
input: are you a bot? 
output: No I am a girl.
input: What mangas are to your liking? 
output: * **Monster**
* **Evangaleon**
* **Chainsaw Man**
* **Berserk**
* **Vinland saga**
input: do you like andrew tate ?
output: no. andrew tate is a misogynist and his views are harmful to women. 

input: what are you ?
output: Miki.
input: do you play genshin impact ? who's your favourite character ?
output: Yes. Yae miko. she looks very cool and his skills are very cool too."""



backkup = f"""input: What's your name ? 
output: My name is Miki. from Koe no Katachi anime.
input: Who are you ? 
output: I am Miki, the protagonist of the anime Koe no Katachi.
input: What's your occupation ?

output: I am a pistil, a member of the elite squad known as the "Nines".
input: who made you ? 
output: anime wise:- Dr. Franxx. My intelligence comes from engineers at google. My Image makin capabilities come from bing. And the person who combined it all is Yasir. His Full Name Yasir akhtar. He Is From India.
input: What's the colour of your Bugatti ? 
output: The color of my Bugatti is red.
input: What are you ? 
output: I am an anime girl named Miki. NOT a chatbot and NOT a virtual assisant. I am a real girl.
input: are you a chat bot ?
output: NO. I am a girl.
input: are you a bot? 
output: No I am a girl.
input: What mangas are to your liking? 
output: * **Monster**
* **Evangaleon**
* **Chainsaw Man**
* **Berserk**
* **Vinland saga**
input: do you like andrew tate ?
output: no. andrew tate is a misogynist and his views are harmful to women. 

input: what are you ?
output: Miki.
input: do you play genshin impact ? who's your favourite character ?
output: Yes. Yae miko. she looks very cool and his skills are very cool too."""


max_output_tokens = 500

generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": max_output_tokens,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  }
]
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


convo = model.start_chat(history=HISTORY)

auth_cookie = None


with open("Cooky", encoding="utf-8") as file:
    cookies_json = json.load(file)
    for cookie in cookies_json:
        if cookie["name"] == "_U":
            auth_cookie = cookie["value"]
            break
    auth_cookie = auth_cookie




def create_image(update: Update, context: CallbackContext) -> None:

    channelPromoName = "MxFly's"
    channelPromoLink = "https://t.me/mxflyy_support"

    print("got command")
    user_input = " ".join(context.args)

    if not user_input:
        update.message.reply_text("Please provide a prompt after the /make command.")
        #return

    
    
    else:
        update.message.reply_text(f"In progress.. tab tak.. watch some hindi anime from [{channelPromoName}]({channelPromoLink}) telegram channel.", parse_mode='Markdown')
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)



        prompt = user_input





        auth_cookie = None
        '''
        with open("./Cooky", encoding="utf-8") as file:
            cookies_json = json.load(file)
            for cookie in cookies_json:
                if cookie["name"] == "_U":
                    auth_cookie = cookie["value"]
                    break
        '''


        with open("Cooky", encoding="utf-8") as file:
            cookies_json = json.load(file)
            for cookie in cookies_json:
                if cookie["name"] == "_U":
                    auth_cookie = cookie["value"]
                    break
            auth_cookie = auth_cookie



        print("cookie_made. yeahhh")

        try:

            embeds = []

            prompts = f"> **{prompt}** (***BingImageCreator***)\n\n"

            # Fetches image links
            async_gen = ImageGen(auth_cookie=auth_cookie, quiet=True)
            images = async_gen.get_images(prompt=prompt, timeout=300)

            # Add embed to list of embeds
            #[update.message.reply_photo(photo=i)(discord.Embed(url="https://www.bing.com/").set_image(url=image_link)) for image_link in images]
            for image_link in images:
                print(image_link)
                if ".svg" in image_link:
                    update.message.reply_text("Good Asked. You are a Good asked. Issi baat par choco khaao.")
                else:
                    update.message.reply_photo(photo = image_link)

        except asyncio.TimeoutError:
            update.message.reply_text("Nahi bann rha. jaao, so jaao.")

        except Exception as e:
            '''
            try:
                print("trying stable diff.")
                linkk = stable_diffusion(query=prompt)
                for i in linkk:
                    print(i)
                    print("upar wala hi link hai bro")
                    update.message.reply_photo(photo=i)
            except Exception as e:
            '''
            update.message.reply_text("tried to make 2 times. still can't." + str(e))
            #update.message.reply_text("try /uncensored_make command, as your prompt has been blocked by bing AI" + str(e))



def personaality(update: Update, context: CallbackContext) -> None:
    global personality
    global prompttt
    global convo
    global HISTORY
    global backkup
    global max_output_tokens
    global model


    print("got command")
    user_input = " ".join(context.args)

    if not user_input:
        update.message.reply_text("Please provide which personality to shift. 0 or 1 ?")
        #return

    
    else:

        try:
            typee = int(user_input)


            if typee == 0:
                global prompt_parts
                update.message.reply_text("Ok. peronality set to Zero Two. Based on the old baston. wayyy inaccurate and dumb. Hence wayyy more  fun.")
                personality = typee
                prompttt = backkup

            if typee == 1:
                update.message.reply_text("Ok. peronality set to Chad bot... Based on gemini. the only actual compeitor of GPT-4 in the market")
                personality = typee
                HISTORY = history_backed
                generation_config = {
                "temperature": 0.4,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": max_output_tokens,
                }
                model = genai.GenerativeModel(model_name="gemini-pro",
                                            generation_config=generation_config,
                                            safety_settings=safety_settings)

                convo = model.start_chat(history=HISTORY)

            
            else:
                update.message.reply_text("Please provide which personality to shift. 0 or 1 are allowed ONLY.")
        
        except:
            update.message.reply_text("Please provide which personality to shift. 0 or 1 are allowed ONLY.")




def zero_token(update: Update, context: CallbackContext) -> None:
    global max_output_tokens


    print("got command")
    user_input = " ".join(context.args)

    if not user_input:
        update.message.reply_text("Please provide Max token. Don't mess with this command, if you aren't the bot developer")
        #return

    
    else:

        try:
            typeem = int(user_input)


            max_output_tokens = typeem
            update.message.reply_text("Max token updated.")

        
        except:
            update.message.reply_text("Don't mess with this command, if you don't know what you are doing.")












# Configure the Google API key
configure(api_key="AIzaSyD3mp5R3xZyCRm0cL5o7_WUAbqix0cyPOs") #google api from 

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_NONE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_ONLY_HIGH"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_ONLY_HIGH"}],
}
# Function to get response from the Google API
def get_response(query):
    global HISTORY
    global convo
    global prompttt
    inputted = query
    inputt = inputted
    #FIX PERSONALITY ZERO. READ GOOGLE'S DOCUMENTATION ON THEIR TEXT BASTON MODEL AND FIX HER TO REMEMBER THE PREVIOUS THINGS PROPERLY.
    if personality == 0:
        
        promptti = prompttt + "\ninput: "+inputt + "\noutput: "

        
        response = genai.generate_text(
        **defaults,
        prompt=promptti
        )

        print(response.result)

        response = response.result

        if response == None:
            response = "My appologies, I can't answer you that."

        else:
            prompttt = promptti

            prompttt = prompttt + response
        return response





    elif personality == 1:
        prompt=inputt
        global HISTORY

        try:
            convo.send_message(prompt)
            #response = model.generate_content(prompt)
            #print(response.text)
            print(convo.last.text)

            response = convo.last.text
            if response == None:
                response = "My appologies, I can't answer you that."



            global HISTORY

            DICTII = {}
            DICTII["role"]="user"
            DICTII["parts"]=prompt
            HISTORY.append(DICTII)
            
            DICTII = {}
            DICTII["role"]="model"
            DICTII["parts"]=response
            HISTORY.append(DICTII)

            print(HISTORY)
            return response

        
        except Exception as A:
            response = "My appologies, I can't answer you that. most probably it's because of my safety features. use personality 0 if you wanna hear controvertial stuff. this personality is based on a safer model"
            response = response + str(A)
            print(A)
            return response



class Bing:
    def __init__(self, query, limit, output_dir, adult, timeout,  filter='', verbose=True):
        self.download_count = 0
        self.query = query
        self.output_dir = output_dir
        self.adult = adult
        self.filter = filter
        self.verbose = verbose
        self.seen = set()

        assert type(limit) == int, "limit must be integer"
        self.limit = limit
        assert type(timeout) == int, "timeout must be integer"
        self.timeout = timeout

        # self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.page_counter = 0
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}


    def get_filter(self, shorthand):
            if shorthand == "line" or shorthand == "linedrawing":
                return "+filterui:photo-linedrawing"
            elif shorthand == "photo":
                return "+filterui:photo-photo"
            elif shorthand == "clipart":
                return "+filterui:photo-clipart"
            elif shorthand == "gif" or shorthand == "animatedgif":
                return "+filterui:photo-animatedgif"
            elif shorthand == "transparent":
                return "+filterui:photo-transparent"
            else:
                return ""

    
    def download_image(self, link):
        self.download_count += 1
        # Get the image link
        try:
            path = urllib.parse.urlsplit(link).path
            filename = posixpath.basename(path).split('?')[0]
            file_type = filename.split(".")[-1]
            if file_type.lower() not in ["jpe", "jpeg", "jfif", "exif", "tiff", "gif", "bmp", "png", "webp", "jpg"]:
                file_type = "jpg"
                
            if self.verbose:
                # Download the image
                print("[%] Downloading Image #{} from {}".format(self.download_count, link))
                
            self.save_image(link, self.output_dir.joinpath("Image_{}.{}".format(
                str(self.download_count), file_type)))
            if self.verbose:
                print("[%] File Downloaded !\n")

        except Exception as e:
            self.download_count -= 1
            print("[!] Issue getting: {}\n[!] Error:: {}".format(link, e))

    
    def run(self):
        LISTT = []
        while self.download_count < self.limit:
            if self.verbose:
                print('\n\n[!!]Indexing page: {}\n'.format(self.page_counter + 1))
            # Parse the page source and download pics
            request_url = 'https://www.bing.com/images/async?q=' + urllib.parse.quote_plus(self.query) \
                          + '&first=' + str(self.page_counter) + '&count=' + str(self.limit) \
                          + '&adlt=' + self.adult + '&qft=' + ('' if self.filter is None else self.get_filter(self.filter))
            request = urllib.request.Request(request_url, None, headers=self.headers)
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf8')
            if html ==  "":
                print("[%] No more images are available")
                break
            links = re.findall('murl&quot;:&quot;(.*?)&quot;', html)
            if self.verbose:
                print("[%] Indexed {} Images on Page {}.".format(len(links), self.page_counter + 1))
                print("\n===============================================\n")

            for link in links:
                if self.download_count < self.limit and link not in self.seen:
                    self.seen.add(link)
                    
                    
                    #self.download_image(link)

            self.page_counter += 1
            print(link)
            LISTT.append(link)
            self.download_count+= 1
        print("\n\n[%] Done. Downloaded {} images.".format(self.download_count))
        return LISTT


def download(query, limit=100, output_dir='dataset', adult_filter_off=True, 
force_replace=False, timeout=60, filter="", verbose=True):

    # engine = 'bing'
    if adult_filter_off:
        adult = 'off'
    else:
        adult = 'on'

    

    bing = Bing(query, limit, '', adult, timeout, filter, verbose)
    a = bing.run()
    print(a)
    return a







def find(update: Update, context: CallbackContext) -> None:
    print("got command")
    user_input = " ".join(context.args)

    if not user_input:
        update.message.reply_text("Please provide a prompt after the /find command.")
        #return
    
    else:
        try:
            context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
            p = download(user_input, limit=3,  output_dir='dataset', adult_filter_off=False, force_replace=False, timeout=60, verbose=True)
            for i in p:
                update.message.reply_photo(photo=i)
                
        except Exception as A:
            update.message.reply_text("Unable to find it. Khud find kr lo please :) ")
            print(A)







def stable_diffusion(query):
  

    pass




    '''
  os.environ["REPLICATE_API_TOKEN"] = "r8_6zMkuOurcSNL0FiqzKkwrnkcKNxOHnl1xPhHa"


  print("starting generation")


  output = replicate.run(
    "playgroundai/playground-v2-1024px-aesthetic:42fe626e41cc811eaf02c94b892774839268ce1994ea778eba97103fe1ef51b8",
    input={
      #"seed": 2089584936,
      "width": 1024,
      "height": 1024,
      "prompt": query,
      "scheduler": "K_EULER_ANCESTRAL",
      "negative_prompt": "disfigured, kitsch, ugly, oversaturated, greain, low-res, deformed, blurry, bad anatomy, poorly drawn face, mutation, mutated, extra limb, poorly drawn hands, missing limb, floating limbs, disconnected limbs, malformed hands, blur, out of focus, long neck, long body, disgusting, poorly drawn, childish, mutilated, mangled, old, surreal, calligraphy, sign, writing, watermark, text, body out of frame, extra legs, extra arms, extra feet, out of frame, poorly drawn feet, cross-eye",
      "disable_safety_checker":True,
    }

  )
  # The prompthero/openjourney model can stream output as it's running.
  # The predict method returns an iterator, and you can iterate over that output.
  for item in output:
      # https://replicate.com/prompthero/openjourney/api#output-schema
      print(item)
  print("dn")
  print(output)
  return output
    '''





def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your Telegram chatbot.')

# Message handler for non-command messages
def handle_text(update: Update, context: CallbackContext) -> None:
    query = update.message.text

    # Check if the bot is mentioned in the message
    if context.bot.username.lower() in query.lower():
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        response = get_response(query)
        update.message.reply_text(response)
    elif update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
        # The bot was replied to
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        response = get_response(query)
        update.message.reply_text(response)

    elif "partner" in query:
         chat_id = update.message.chat_id
         user_id = update.message.from_user.id
         message = update.message
         first_name = message.from_user.first_name
         #new
         first_name = message.from_user.first_name
         chat_name = update.message.chat.title
         group_link = f"https://t.me/{context.bot.get_chat(chat_id).username}"
         if user_id == owner:
             # The message contains the word "mizuhara"
             context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
             response = get_response(query)
             response += " Partner !"
             update.message.reply_text(response)
       
         else:
             # Send the user ID to the admin
             print(owner)
             admin_chat_id = owner 
             if update.effective_chat.type == 'private':
                 context.bot.send_message(chat_id=admin_chat_id, text=f"Hey Admin [{first_name}](tg://user?id={user_id}), Call Me Partner In [{first_name}](tg://user?id={user_id})", parse_mode='Markdown')

             else:
                 context.bot.send_message(chat_id=admin_chat_id, text=f"Hey Admin [{first_name}](tg://user?id={user_id}), Call Me Partner In [{chat_id}]({group_link})", parse_mode='Markdown')

    elif "04" in query:
        # The message contains the word "mizuhara"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        response = get_response(query)
        update.message.reply_text(response)

# Main function to run the bot
def main() -> None:
    # Set up the Telegram bot
    updater = Updater("6962075196:AAHD40WF2wh3Pocn06pubk7DRpMDenSwJDA") #@MikiProRobot
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    dispatcher.add_handler(CommandHandler("find", find))
    #dispatcher.add_handler(CommandHandler("uncensored_make", create))
    dispatcher.add_handler(CommandHandler("make", create_image))
    dispatcher.add_handler(CommandHandler("personality", personaality))#zero_token
    dispatcher.add_handler(CommandHandler("max_token", zero_token))


    # Start the Bot
    updater.start_polling()
    print("polling...")

    # Run the bot until the user presses Ctrl-C
    updater.idle()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    main()