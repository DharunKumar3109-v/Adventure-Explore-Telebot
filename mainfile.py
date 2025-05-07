import telebot
from telebot import types 


bot_token = '6561067742:AAEA79kn-xKB-ENLVkrAmvJxn3H4Yh5wHRQ'
bot = telebot.TeleBot(bot_token)

# Define states and corresponding touristplace
state_map={
    'Jammu And Kashmir':['Vaishno Devi','Sri Shankaracharya Temple','Wadiy e Hajan','Tulip Garden Srinagar','Shah Kashmir Arts Emporium','hri Amarnath Cave Temple','Sinthan Top','Dal Lake','Shalimar Bagh Mughal Garden','Nigeen Lake'],
    'Himachal Pradesh' :['Shimla','Kullu-Manali','Dharamshala and McLeodganj','Dalhousie','Khajjiar','Kasol','Kasauli','Kufri','Palampur','Kangra'],
    'Panjab' : ['Amritsar','Ludhiana','Jalandhar','Bathinda'],
    'Nepal' : ['Bhaktapur','Chitwan National Park','Lumbini','Pokhara','Kathmandu'],
    'Delhi' : ['Chandni Chowk','Hauz Khas','Qutab Minar','Red Fort','India Gate'],
    'Uttarakhand' : ['Harsil','Munsiyari','Utha','Chakrata','Mussoorie','Nainital','Auli'],
    'Rajasthaan' : ['Ranthambore Tiger Reserve','touristspot Palace of Jaipur','Hawa Mahal - Palace of Wind','Lake Pichola','touristspot Palace of Udaipur','Elefantastic','Mehrangarh Fort'],
    'Uttar Pradesh' : ['Taj Mahal','Wildlife Sos','Assi Ghat','Agra Fort'],
    'Bihar' : ['Kesaria','Pawanpuri','Rajgir','Vaishali','Nalanda','Bodhgaya'],
    'West Bengal' : ['Kurseong','Kalimpong','Dooars','Mirik','Siliguri','Sundarbans','Darjeeling','Kolkata'],
    'Jharkhand' : ['Dhanbad','Deoghar','Jamshedpur','Ranchi'],
    'Chhattisgarh' : ['Chitrakote Falls','Madku Dweep','Mainpat','Charre Marre Waterfalls','Jagdalpur','Barnawapara Wildlife Sanctuary'],
    'Madhya Pradesh' : ['Gwalior','Pachmarhi','Khajuraho','Rajwada Palace','Bhimbetka rock shelters','Kanha Tiger Reserve','Bhedaghat'],
    'Gujarat' : ['Somnath Temple','Laxmi Vilas Palace','Adalaj Stepwell','Sabarmati Ashram','Shree Dwarkadhish Temple','Gir National Park','Statue Of Unity'],
    'Maharashtra' : ['Malshej Ghat','Chhatrapati Shivaji Maharaj Terminus','Ajanta Caves','Ellora Caves','Gateway Of India Mumbai','Fort Raigad','Tadoba-Andhari Tiger Reserve'],
    'Odisha' : ['Bhitarkanika National Park','Udayagiri','Chilika Lake','Konark','Bhubaneswar','Puri'],
    'Telungana' : ['Nizamabad','Nalgonda','Adilabad','Bhadrachalam','Warangal','Nagarjunasagar','Hyderabath'],
    'Andhara Pradesh' : ['Vijayawada','Tirupati','Gandikota','Amaravathi','Visakhapatnam','Araku Valley'],
    'Karnataka' : ['Chikmagalur','Jog Falls','Udupi','Gokarna','Hampi','Badami','Coorg'],
    'Kerala' : ['Idukki','Kollam','Poovar','Kovalam','Vagamon','Varkala','Wayanad','Kochi','Munnar'],
    'Tamil Nadu' : ['Kolli Malai','Kutralam','Yelagiri','Velankanni','Coonoor','Mahabalipuram','Hogenakkal','Ooty','Kodaikanal','Yercaud'],
    'Arunachal Pradesh' : ['Roing','Tezu','Sela Pass','Namdapha National Park','Ziro Valley','Tawang'],
    'Assam' : ['Dibrugarh','Manas National Park','Jorhat','Guwahati','Majuli'],
    'Nagaland' : ['Pfutsero','Khonoma Village','Tuensang','Kohima'],
    'Manipur' : ['Tamenglong','Thoubal','Chandel','Khongjom','Andro'],
    'Mizoram' : ['Reiek Tlang','Champhai','Lunglei']
}


# Define blood types
Hotel_types= ['Hotel']

user_state_map = {}
user_touristspot_map = {}
user_hotel_map = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['/search_the_state']
    buttons1 = ['/help', '/stop', '/Creater']
    markup.add(*[types.KeyboardButton(button) for button in buttons])
    markup.add(*[types.KeyboardButton(button) for button in buttons1])

    bot.reply_to(message, "I am a Tourist bot. How can I help you?", reply_markup=markup)

@bot.message_handler(commands=['stop'])
def stop_command(message):
    bot.reply_to(message, "Thank you for using me!")

@bot.message_handler(commands=['Creater'])
def owner_command(message):
    bot.reply_to(message, "I was created by Dharun")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "I am a Tourist bot. Kindly provide me details for further response")

@bot.message_handler(commands=['search_the_state'])
def state_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Create buttons for all states
    state_buttons = [types.KeyboardButton(state) for state in state_map.keys()]
    markup.add(*state_buttons)

    bot.reply_to(message, 'Select the state:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in state_map.keys())
def handle_state_selection(message):
    selected_state = message.text
    user_state_map[message.chat.id] = selected_state

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Create buttons for touristplace based on the selected state
    touristspot_buttons = [types.KeyboardButton(touristspot) for touristspot in state_map[selected_state]]
    markup.add(*touristspot_buttons)

    bot.reply_to(message, f'Select the touristspot in {selected_state}:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [touristspot for touristplace in state_map.values() for touristspot in touristplace])
def handle_touristspot_selection(message):
    selected_touristspot = message.text
    user_touristspot_map[message.chat.id] = selected_touristspot

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Create buttons for Hotel types
    Hotel_types_buttons = [types.KeyboardButton(Hotel_types) for Hotel_types in Hotel_types]
    markup.add(*Hotel_types_buttons)

    bot.reply_to(message, f'Select your touristplace in {selected_touristspot}:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in Hotel_types)
def handle_Hotel_types_selection(message):
    selected_Hotel_types = message.text
    user_hotel_map[message.chat.id] = selected_Hotel_types

    # Now you can retrieve the list of tourist based on the selected state, touristspot, and blood type
    selected_state = user_state_map.get(message.chat.id)
    selected_touristspot = user_touristspot_map.get(message.chat.id)

    if selected_state and selected_touristspot:
        # Retrieve  based on the selected criteria (you can replace this with your actual data)
        tourist = get_tourist(selected_state, selected_touristspot, selected_Hotel_types)

        if tourist:
            response = f'tourist with Hotel type {selected_Hotel_types} in {selected_touristspot}, {selected_state}:\n'
            for tourist in tourist:
                response += f'{tourist["name"]}\n'
        else:
            response = f'No tourist  {selected_Hotel_types} in {selected_touristspot}, {selected_state}.'

        bot.reply_to(message, response, reply_markup=None)
    else:
        bot.reply_to(message, 'Please select state, touristspot, and Hotel types first.')

# Function to simulate retrieving tourist (replace this with your actual data retrieval logic)
def get_tourist(state,touristspot,Hotel_types):
    # This is a placeholder. You should replace this with your actual data retrieval logic.
    # The structure of tourist should be a list of dictionaries with 'name' and 'contact' keys.

       
    if state == 'Tamil Nadu':
        if touristspot == 'Kolli Malai':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'RVR Rejoice Villa Resorts Kolli Hills'},
                    {'name': 'Seattle Garden KolliHills'},
                    {'name': 'RJ Grand Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Kutralam':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Jijis Castle'},
                    {'name': 'The Pothigai Palace'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Yelagiri':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Rhythms Lake View Resorts'},
                    {'name': 'J P Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Velankanni':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'ANNAI OCEAN PARK'},
                    {'name': 'HOTEL ANNAI BAY'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Coonoor':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The Birdhouse Hostel'},
                    {'name': 'The Highgarden Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Mahabalipuram':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hangout Beach Stay'},
                    {'name': 'Hotel Daphne Mahabalipuram'},

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Hogenakkal':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Sri Priya Lodge'},
                    {'name': 'Amman Cottage'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Ooty':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Gangas Sri Balaji Cottage'},
                    {'name': 'goSTOPS OOTY'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Kodaikanal':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Lumino Fairstay'},
                    {'name': 'Zostel Kodaikanal'}

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Yercaud':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel GVS Residency'},
                    {'name': 'Hotel R Inn Yercaud'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist   
    elif state == 'Andhara Pradesh':
        if  touristspot == 'Vijayawada':
            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Treebo Trend Madhuvan Grand'},
                    {'name': 'HOTEL MINERVAHotel Kosala'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
            
        if touristspot == 'Tirupati':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Pearl Suites'},
                    {'name': 'HOTEL PARK KRISHNA'},
                    {'name': 'Hotel Elite Park'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Gandikota':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel YLN GRAND'},
                    {'name': 'Royal Palace Residency'},
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Amaravathi':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Treebo Trend Arka Vijayawada'},
                    {'name': 'HOTEL MINERVA'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Visakhapatnam':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Treebo Trend Celeste'},
                    {'name': 'Hotel Apna Taj Residency'},
                    {'name': 'Homey Meadows'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
        if touristspot == 'Araku Valley':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Bansi Resorts'},
                    {'name': 'Natures Nest Araku'},
                    {'name': 'Casa Holiday Resorts'}

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist
    elif state ==  'Kerala':
        if touristspot == 'Idukki':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Meghamala Resorts'},
                    {'name': 'Hotel Idukki Castle'},
                    {'name': 'IGLOO HERITAGE HOTELS'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Kollam':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Zaina Tourist home'},
                    {'name': 'Chandra Inn'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Poovar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Meridian By Daan'},
                    {'name': 'Poovar Sea View'},
                    {'name': 'Meridian By Daan,Poovar Sea View'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kovalam':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Neptune Kovalam'},
                    {'name': 'New Volga Palace Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Vagamon':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Vaga View'},
                    {'name': 'Honeycomb'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Varkala':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Cliff County Varkala'},
                    {'name': 'SCliff Beach Resort Varkala'},
                    {'name': 'Cliff & Coral'}

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Wayanad':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Vythiri Stream View'},
                    {'name': 'Vythiri Mist Resort'},
                    {'name': 'Mangosteen Holidays'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kochi':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'SpringField Billets Hotel'},
                    {'name': 'Hotel Mart View'}

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Munnar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Arul Mount'},
                    {'name': 'Munnar Cottage by Bookingmania'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'West Bengal':
        if touristspot == 'Kurseong':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Queens Hill Hotel & Resort'},
                    {'name': 'Hotel Bashera Kurseong'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Kalimpong':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Kalimpong Sunrise Inn Homestay'},
                    {'name': 'The Atrium Park'},
                    {'name': 'Mystic Orchid Retreat'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Dooars':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Tuskers Den Forest Resort'},
                    {'name': 'Aranya Jungle Resort'},
                    {'name': 'The Reserve Gorumara'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Mirik':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Jagjeet Hotel'},
                    {'name': 'Golden Sunview Homestay'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Siliguri':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The Imperial Inn'},
                    {'name': 'Hiland Hotel'},
                    {'name': 'Hotel Saluja'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Sundarbans':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Prakrity Village Resort Sundarbans'},
                    {'name': 'Hotel Sonar Bangla'},
                    {'name': 'Sundarban Tiger Roar Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Darjeeling':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Vantage Point Homestay'},
                    {'name': 'The Revett'},
                    {'name': 'Darjeeling Holiday Home'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kolkata':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The LaLiT Great Eastern Kolkata'},
                    {'name': 'The Elite Apartment Hotel'}
                    # Add more tourist as needed
                ]  
            else:
                tourist = []   
            return tourist  
    elif state == 'Arunachal Pradesh':
        if touristspot == 'Roing':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Dibang Valley Jungle Camp'},
                    {'name': 'Jia Organic Eco Resort'},
                    {'name': 'Mito Hotel Homestay'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Tezu':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Mito Hotel Homestay'},
                    {'name': 'Hotel Nam LauHotel Nam Lau'},
                    {'name': 'Golden Pagoda Eco Resort'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Sela Pass':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Letro Home Stay'},
                    {'name': 'Dirang Boutique Cottages'},
                    {'name': 'Lanjom Homestay'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Namdapha National Park':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Golden Pagoda Eco Resort'},
                    {'name': 'Hotel Nam Lau'},
                    {'name': 'Namdapha Jungle Camp'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Ziro Valley':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Anne Ziro'},
                    {'name': 'Siiro Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Tawang':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The Oak Tawang'},
                    {'name': 'Hotel Tawang HeightsHotel Tawang Heights'},
                    {'name': 'Hotel Menda-La Tawang'}

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Assam':
        if touristspot == 'Dibrugarh':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Tree Fern'},
                    {'name': 'Comfort Hotel'},
                    {'name': 'Raj Meridian Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Manas National Park':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hornbill Eco Camp'},
                    {'name': 'Eagle Nest Eco Retreat'},
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Jorhat':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Taj Heritage Hotel and Homestay'},
                    {'name': 'D Royal Palm'},
                    {'name': 'Hotel Gulmohar Grand'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Guwahati':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Radisson Blu Hotel'},
                    {'name': 'Hotel Gateway Grandeur'},
                    {'name': 'Hotel Guwahati Inn'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Majuli':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Risong Family Guest house'},
                    {'name': 'Okegiga Homes'},
                    {'name': 'River wind cottage'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Bihar':
        if touristspot == 'Kesaria':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'SPOT ON 70255 Hotel Laxmi International'},
                    {'name': 'SPOT ON 64941 Awasiya Subhash Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Pawanpuri':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Chirag'},
                    {'name': 'Hotel MJ Royale Bikaner'},
                    {'name': 'Hotel Rajdarbar Inn'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Rajgir':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Sagar Inn'},
                    {'name': 'Hotel Diamond Plaza'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Vaishali':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Madhu Vatika'},
                    {'name': 'Bandhan Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == ' Nalanda':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Nalanda Guest House'},
                    {'name': 'Hotel Diamond Plaza'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Bodhgaya':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Laxmi international bodhgaya'},
                    {'name': 'The Royal Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Chhattisgarh':
        if touristspot == 'Chitrakote Falls':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'STF camp resort'},
                    {'name': 'Dandami Luxury Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Madku Dweep':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Central Point International'},
                    {'name': 'Mittan Resort'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Mainpat':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Dolma Tibet Resort'},
                    {'name': 'Karma Ethnic Resort'},
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Charre Marre Waterfalls':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': ' Hotel Green Palm'},
                    {'name': 'Kanker Palace Heritage'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Jagdalpur':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Champa Baag Resort'},
                    {'name': 'Binaka Heritage'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Barnawapara Wildlife Sanctuary':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Barn Field Villa'},
                    {'name': 'Bardiha Lake View Tourist Cottages'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Delhi':
        if touristspot == 'Chandni Chowk':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Le ROI Express Paharganj'},
                    {'name': 'Hotel Tara Palace Daryagan'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == ' Hauz Khas':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Woodpecker Apartment '},
                    {'name': 'Haveli Hauz Khas'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Qutab Minar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Lemonwood Suites By F9 Hotels'},
                    {'name': 'FabExpress The Premium Villa - Hotel '}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Red Fort':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Tara Palace Daryaganj'},
                    {'name': 'Homestay AC Dormitory'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'India Gate':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Royal Rosette'},
                    {'name': 'The Corus Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Gujarat':
        if touristspot == 'Somnath Temple':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The Bliss Hotel'},
                    {'name': 'Hotel Avadh'},
                    {'name': 'HOTEL PLATINUM'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Laxmi Vilas Palace':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'FabHotel Prime Palace View'},
                    {'name': 'Hotel Marigoldv'},
                    {'name': 'Laxmi Vilas Palace'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Adalaj Stepwell':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel German Palace'},
                    {'name': 'Tribecca SelectSiara Styles Amba Suites'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Sabarmati Ashram':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Toran Hotel'},
                    {'name': 'SilverCloud Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Shree Dwarkadhish Temple':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel lord krishna'},
                    {'name': 'Hotel The Grand Ladhukara'},
                    {'name': 'Devbhoomi ResidencyDevbhoomi Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Gir National Park':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'KAVISH GIR LION RESORT'},
                    {'name': 'Pride Biznotel'},
                    {'name': ' Sasan Gir'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Statue Of Unity':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The Grand Unity Rooms'},
                    {'name': 'Ramada Encore By Wyndham Statue of Unity'},
                    {'name': 'Hotel BRG Budget Stay'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Hariyana':
        if touristspot == 'Manesar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'HOTEL GURUGRAM MANESAR'},
                    {'name': 'Hotel Manesar'},
                    {'name': 'Hotel Elite Oak'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Kalesar National Park':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Kasauli Nature INN'},
                    {'name': 'Pacific Inn Hotel'},
                    {'name': 'Hotel The Grands'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Damdama Lake':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Touchwood Inn'},
                    {'name': 'The Gateway Resort Damdama Lake Gurgaon'},
                    {'name': 'Botanix Nature Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Sultanpur Bird Sanctuary':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Natraj Greens Dev farm'},
                    {'name': 'The Mango Tree - By Shay Hospitality'},
                    {'name': 'Natraj Greens Dev farm'}
    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Panchkula':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Chandigarh Grand and Banquet'},
                    {'name': 'Hotel Lamp Inn PanchkulaHotel Chandigarh Grand and Banquet'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Himachal Pradesh':
        if touristspot == ' Shimla':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'THE HARITAGE HOTEL SHIMLA'},
                    {'name': 'Solo Home Shimla'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Dharamshala and McLeodganj':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'White Water Inn McLeodgan'},
                    {'name': 'Hotel The Nest'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Dalhousie':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Heaven Hills'},
                    {'name': 'Hotel Dalhousie Heights'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Khajjiar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Khajjiar Regency'},
                    {'name': 'Colors of Himalaya - Garg Woods Villa'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == ' Kasol':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Kasol Inn'},
                    {'name': 'The Hosteller Kasol'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kasauli':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Orchid Kasauli'},
                    {'name': 'Hotel Kasauli Regency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kufri':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Kufri Holiday Inn'},
                    {'name': 'Sterling Kufri'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Palampur':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Raj Golden'},
                    {'name': 'Hotel Peak Bound'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kangra':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Clarks Inn Suites'},
                    {'name': 'Comfort stay kangra'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Jammu':
        if touristspot == 'Vaishno Devi':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Suman'},
                    {'name': 'Ganpati Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Sri Shankaracharya Temple':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Sahara Grand Hills'},
                    {'name': 'Hotel Lime Wood Inn'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Wadiy e Hajan':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Zebrina Pahalgam'},
                    {'name': 'The Pahalgam Pines By Sarwar Resorts'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Tulip Garden Srinagar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Zostel Srinagar'},
                    {'name': 'Whostels Srinagar'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Shah Kashmir Arts Emporium':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Zostel Srinagar'},
                    {'name': 'touristspot Of Kashmir'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Sinthan Top':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The Chamba Resort and Camps'},
                    {'name': 'SHEESHAM RESORT'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Dal Lake':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Kashmir Inn'},
                    {'name': 'Zostel Srinagar'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Shalimar Bagh Mughal Garden':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Pallas Inn & Suites-RESORTS'},
                    {'name': 'Savera Inn Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Nigeen Lake':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Lake View Resort By(J.V)'},
                    {'name': 'Hotel Sultan Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Jharkhand':
        if touristspot == 'Dhanbad':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Eden Blu'},
                    {'name': 'Hotel Prakash Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Deoghar':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Shanti Niketan'},
                    {'name': 'Hotel Ganga Palace'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Jamshedpur':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Ganga Regency'},
                    {'name': 'THE PEARL HOTEL'},
                    {'name': 'Ramada'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Ranchi':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Meera,Hotel Sohrai inn'},
                    {'name': 'Treebo Trend Winsome Banquet And Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Karnataka':
        if touristspot == 'Chikmagalur':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Treebo Trend Lucent'},
                    {'name': 'Hotel New Empire'},
                    {'name': 'Trippr Chikkamagaluru'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Jog Falls':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Jog Sharadha Homestay'},
                    {'name': 'Tirumala Comfort Hotel'},
                    {'name': 'Hotel Mayura Gersoppa Jogfalls'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Udupi':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Udupi Residency'},
                    {'name': 'Meenakshi Inn'},
                    {'name': 'Hotel Sri Krishna Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Gokarna':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Paradise Holiday Cottages'},
                    {'name': 'Golden Heights-Gokarna'},
                    {'name': 'Vibes and Tides Beach Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Hampi':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Hampi International'},
                    {'name': 'Hotel Malligi Hampi'},
                    {'name': 'LAKSHMI HERITAGE TOURIST HOME'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == ' Badami':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Morpho Banashree Resort'},
                    {'name': 'Hotel Chandra Palace'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Coorg':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Treebo Trend Oleander Serviced Apartments'},
                    {'name': 'Coorg Home stay'},
                    {'name': 'Hotel Coorg Palace'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Madaya Pradesh':
        if touristspot == 'Gwalior':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Ramaya'},
                    {'name': 'Clarks Inn Suites Gwalior'},
                    {'name': 'Hotel Landmark'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Pachmarhi':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'WOWSTAYZ Pachmarhi Ecotel Resort',},
                    {'name': 'Pandav Residency'},
                    {'name': 'Hotel Himalaya Pachmarhi'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Khajuraho':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Bundela Resort Khajuraho'},
                    {'name': 'Hotel Ramayana Khajuraho'},
                    {'name': 'HOTEL KHAJURAHO INN'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Rajwada Palace':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Lakshya Sheesh Mahal Indore'},
                    {'name': 'Hotel touristspot Pride'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Bhimbetka rock shelters':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Wisteria Blue'},
                    {'name': 'Hotel Shiv Shakti'},
                    {'name': 'Hotel Meenakshi Rooms'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kanha Tiger Reserve':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Tuli Tiger Resort'},
                    {'name': 'MPT Jungle Resort Sarhi'},
                    {'name': 'MOGLI RESORT'}

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Bhedaghat':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Royal Orbit,'},
                    {'name': 'Hotel Satyam Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Maharashtra':
        if touristspot == '':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Blu Water Resort Malshej'},
                    {'name': 'Saj By The Lake: Luxury Resort'},
                    {'name': 'MTDC Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Chhatrapati Shivaji Maharaj Terminus':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'West End Hotel'},
                    {'name': ' Empire Royale Hotel '},
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Ajanta Caves':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Royal Ajanta Park'},
                    {'name': 'Agrawals restaurant and lodging'},
                    {'name': 'Hotel ajanta green restaurant '}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Ellora Caves':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Kailas'},
                    {'name': 'Ellora Heritage Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Gateway Of India Mumbai':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Grace galaxy'},
                    {'name': 'The Royal Orchid'},
                    {'name': 'Empire Royale Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Fort Raigad':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Jay bhavani farm house raigad fort'},
                    {'name': 'Sahyadri hotel'},
                    {'name': 'Hirkani Aangan'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Tadoba-Andhari Tiger Reserve':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Avadale Tadoba'},
                    {'name': 'Tadoba Tiger Valley Resort'},
                    {'name': 'Hotel Tiger Inn'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Nagaland':
        if touristspot == 'Pfutsero':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'de Oriental Grand'},
                    {'name': 'Niraamaya Retreats Aradura'},
                    {'name': 'Native Stories'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Khonoma Village':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Niraamaya Retreats Aradura'},
                    {'name': 'Pier Vantage Homestay Khonoma'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Tuensang':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Tairas'},
                    {'name': '2K Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kohima':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The Palm Guest House'},
                    {'name': 'Niraamaya Retreats Aradura'},
                    {'name': 'The East Gate Hotel'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Nepal':
        if touristspot == 'Bhaktapur':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Swastik Guest House'},
                    {'name': 'Hotel Bhaktapur Inn'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Chitwan National Park':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Tiger Residency Resort'},
                    {'name': 'Chital Lodge'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Lumbini':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Peaceland Lumbini'},
                    {'name': 'Lumbini Village Lodge'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Pokhara':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Eagle Zone'},
                    {'name': 'Hotel Mountain View'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Kathmandu':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Kathmandu Peace Homev'},
                    {'name': 'Nepal Pavilion Inn'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Odisha':
        if touristspot == 'Bhitarkanika National Park':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Sand Pebbles Bhitarkanika Jungle Resorts'},
                    {'name': 'Bhitarkanika Eco Resorts'},
                    {'name': 'JUNGLE AVENGERS RESORT'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Udayagiri':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Cherukuri Grand',}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Chilika Lake':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'OTDC Panthanivas - Rambha'},
                    {'name': 'Chilika Heritage Resort'},
                    {'name': 'Swosti Chilika Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Konark':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Kings Coco Resort'},
                    {'name': 'HOLIDAY INN'},
                    {'name': 'Sun Temple Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Bhubaneswar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Greenland Premium Hotel'},
                    {'name': 'Mango Hotels'},
                    {'name': 'Hello Stay Hotel Bhubaneswar'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Puri':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Sea View Residency'},
                    {'name': 'Hotel Golden Palace Puri'},
                    {'name': 'Sterling Puri'}

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Punjab':
        if touristspot == 'Amritsar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Grand Fortune'},
                    {'name': 'Ramada by Wyndham Amritsar'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Ludhiana':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Kohinoor Palace & Banquets'},
                    {'name': 'Hotel The Retro Regency'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Jalandhar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Kohinoor Palace & Banquets'},
                    {'name': 'Hotel The Retro Regency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Bathinda':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Stella Hotel,Hotel Marbela'},
                    {'name': 'Hotel Marbela'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Uttarakhand':
        if touristspot == 'Ranthambore Tiger Reserve':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hoter & Resort'},
                    {'name': 'The Fern Ranthambhore Forest Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'touristspot Palace of Jaipur':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Rajasthan Palace'},
                    {'name': 'Hotel Arco Palace Jaipur'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Hawa Mahal':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Wind Palace'},
                    {'name': 'Khandaka Mahal'},
                    {'name': 'Virasat Mahal Heritage Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Lake Pichola':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Ram Pratap Palace'},
                    {'name': 'Hotel Sarovar'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'touristspot Palace of Udaipur':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Royal Heritage Villa HomeStay'},
                    {'name': 'Hotel Udai Palace'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Elefantastic':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Vesta Maurya Palace'},
                    {'name': 'Jaipur Hotel New'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Mehrangarh Fort':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'blue stay Jodhpur'},
                    {'name': 'Gouri Heritage Haveli'},
                    {'name': 'Krishna Prakash Heritage Haveli'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Telungana':
        if touristspot == 'Nizamabad':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Sri Rama Lodge'},
                    {'name': 'Nakshatra Inn'},
                    {'name': 'HOTEL TRP BLISS'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Nalgonda':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Vivera',},
                    {'name': 'Swagath Residency'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Adilabad':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel New Krishna Lodge'},
                    {'name': 'Hotel Radhe Krishna'},
                    {'name': 'Hotel Sai Panchvati'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Bhadrachalam':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'SRI BHAVYA RESIDENCY'},
                    {'name': 'SRI BHAVYA RESIDENCY'},
                    {'name': 'Srinidhi Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Warangal':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'HOTEL ML GRAND'},
                    {'name': 'Hotel Prime Inn'},
                    {'name': 'HOTEL THOUSAND PILLARS'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Nagarjunasagar':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'G.V GRAND'},
                    {'name': 'Nagarjuna Sagar Resort'}

                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Hyderabath':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Aditya Park Sarovar Portico Hyderabad'},
                    {'name': 'Hotel Grand Himayat'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    elif state == 'Uttar Pradesh':
        if touristspot == 'Taj Mahal':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Atulyaa Taj'},
                    {'name': 'Hotel Taj Resorts'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Wildlife Sos':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': ' Goverdhan Palace'},
                    {'name': 'Bhawna Clarks Inn'},
                    {'name': 'GenX Agra'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Assi Ghat':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Palace on Ganges'},
                    {'name': 'Rivera Palace'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Agra Fort':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Marygold Agra'},
                    {'name': 'Sukoon Home Stay Agra'}
                    # Add more tourist as needed
                ] 
            else:
                tourist = []   
            return tourist 
    elif state == 'Uttarakhand':
        if touristspot == ' Harsil':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Hotel Royal Hillcrest'},
                    {'name': 'Harsil Retreat'},
                    {'name': 'Hotel Royal Hillcres'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
            
        if touristspot == 'Munsiyari ':


            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Mount Kailash Homestay & Guest House'},
                    {'name': 'Hotel Laxmi Lodge'}
                    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Rishikesh':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Moustache Rishikesh Luxuria'},
                    {'name': 'Zostel Rishikesh (Tapovan)'},
                    {'name': 'Hotel Aqua Vibes'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Chakrata':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Dopaar by the Brook'},
                    {'name': 'Chakrata Pacific Resort & Spa'},
                    {'name': 'Snow View Heritage Resort Chakrata'}
    
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Mussoorie':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'goSTOPS Mussoorie Picture Palace'},
                    {'name': 'Zostel Mussoorie (Mall Road)'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Nainital':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Orchid Nainital'},
                    {'name': 'India Hotel'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Auli':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'The Tattva'},
                    {'name': 'Faraway Cottages Faraway Cottages'},
                    {'name': 'Blue Poppy Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Shalimar Bagh Mughal Garden':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Pallas Inn & Suites-RESORTS'},
                    {'name': 'Savera Inn Resort'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
        if touristspot == 'Nigeen Lake':

            if Hotel_types == 'Hotel':
                tourist = [
                    {'name': 'Lake View Resort By(J.V)'},
                    {'name': 'Hotel Sultan Residency'}
                    # Add more tourist as needed
                ]
            else:
                tourist = []   
            return tourist 
    else:
        tourist =[]  # Return an empty list for other blood types
    return tourist      
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    bot.reply_to(message, "You can control me by sending these commands:\n/start - start bot\n/help - helps you\n/Creater - owner\n/stop- stop the bot", reply_markup=None)

# Polling loop to keep the bot running
print("Starting the bot....")
bot.polling()
