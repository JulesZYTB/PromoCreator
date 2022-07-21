import requests, random, string, time, colorama, art, user_agent, gratient
import os

class Color:
      def __init__(self) -> None:
          pass

      def red_gratient(self, text = None):
          return gratient.red(text).strip()

      def green_gratient(self, text = None):
          return gratient.green(text).strip()

      def log_success(self, text):
          print(f'[{self.green_gratient("*")}] | %s' % (text))
          print

      def log_invalid(self, text):
          print(f'[{self.red_gratient("*")}] | %s' % (text))
          print
  
class Medal:
      def __init__(self) -> None:
          pass

      def deleteAccount(self, userAgent, userId, medalToken, proxy = None):
          return requests.delete(
                 'https://medal.tv/api/users/%s' % (userId),
                  headers = {
                          'Accept'           : 'application/json',  
                          'Content-Type'     : 'application/json',
                          'User-Agent'       :  userAgent,
                          'Medal-User-Agent' :  userAgent,
                          'X-Authentication' :  medalToken,                
                  }, proxies = {
                             'http'     : f'http://{proxy}'  , 
                             'https'    : f'http://{proxy}'
                  } if proxy != None else None
          ).json()
        
      def getConnections(self, userAgent, medalToken, proxy = None):
          return requests.post(
                 'https://medal.tv/social-api/connections',
                  headers = {
                          'Accept'           : 'application/json',  
                          'Content-Type'     : 'application/json',
                          'User-Agent'       :  userAgent,
                          'Medal-User-Agent' :  userAgent,
                          'X-Authentication' :  medalToken,
                  }, json = {'provider'      : 'discord'},
                  proxies = {'http'  : f'http://{proxy}'  , 'https'    : f'http://{proxy}'} if proxy != None else None
          ).json()

      def sendWebhook(self, webhookUrl, userAgent, userToken, nitroCode, tokenUsed):
          requests.post(
                   webhookUrl,
                   json = {
                        'embeds': [
                                {
                                    'title'        : 'Promotion Code Generated',
                                    'color'        :  3092790,
                                    'fields'       :  [
                                                   {
                                                        'name'    : 'Nitro Link',
                                                        'value'   : '**%s**' % (nitroCode),
                                                        'inline'  :  True
                                                   }, {
                                                        'name'    : 'Medal.TV Token',
                                                        'value'   : '`%s`' % (userToken),
                                                        'inline'  :  True
                                                   }, {'name'     : 'Discord Token', 'value': '`%s**`' % (tokenUsed[:29]), 'inline': True}, {
                                                        'name'    : 'User Agent Used',
                                                        'value'   : '```\n%s```' % (userAgent),
                                                        'inline'  :  False
                                                   }
                                    ], 'footer'   : {
                                                  'text': 'PromoCreator V 1.0.1'
                                    }
                                }
                        ]
                   }
          )
      def createAuthentication(self, userEmail, userPassword, proxy = None):
          if True:
             userAgent   = user_agent.generate_user_agent()
             userAgent
            
          return requests.post(
                 'https://medal.tv/api/authentication',
                  headers = {
                          'Accept'           : 'application/json',  
                          'Content-Type'     : 'application/json',
                          'User-Agent'       :  userAgent,
                          'Medal-User-Agent' :  userAgent,
                  }, json = {'email' : userEmail          , 'password' : userPassword},
                  proxies = {'http'  : f'http://{proxy}'  , 'https'    : f'http://{proxy}'} if proxy != None else None
          ).json()
        
      def createAccount(self, authorizationToken, deleteAfter = False, proxy = None, webhookUrl = None):
          if True:
             if True:
                accountGenerated = False
                accountAttempts  = 0
                accountUserAgent = user_agent.generate_user_agent()

             while accountGenerated == False:
                   email    = ''.join(random.choice(string.ascii_letters) for x in range(7)) + random.choice(['@gmail.com', '@yahoo.com'])
                   username = ''.join(random.choice(string.ascii_letters) for x in range(7))
                   password = ''.join(random.choice(string.ascii_letters) for x in range(10))

                   if accountAttempts == 5:
                      return None
                      break
                      
                   if accountAttempts != 5:
                      resp = requests.post(
                             'https://medal.tv/api/users',
                              headers = {
                                      'Accept'           : 'application/json',
                                      'User-Agent'       : '%s' % (accountUserAgent),
                                      'Medal-User-Agent' : '%s' % (accountUserAgent),
                              }, json = {
                                      'email'            : '%s'    % (email),
                                      'userName'         : '%s'    % (username),  
                                      'password'         : '%s'    % (password),
                              }, proxies = {
                                         'http'     : f'http://{proxy}'  , 
                                         'https'    : f'http://{proxy}'
                              } if proxy != None else None
                      )

                      if resp.ok:
                         accountGenerated = True
                         break
                        
                      accountAttempts += 1
                      accountAttempts, Color().log_invalid(text = 'Failed Attempt | %s' % (accountAttempts))

             if accountGenerated == True:
                try:
                   if True:
                      if True:
                         authenticationResponse = self.createAuthentication(email, password, proxy if proxy != None else None)
                         authenticationResponse
                        
                      userId       = authenticationResponse['userId']
                      key          = authenticationResponse['key']

                      Color().log_success('Account Created | %s' % (f'{userId},{key}'[:18]))

                   discordData     = self.getConnections(accountUserAgent, f'{userId},{key}', proxy if proxy != None else None)
                   discordAuthUrl  = discordData['loginUrl'] 
                   discordAuthResp = requests.post(
                                     discordAuthUrl,
                                     headers = {
                                             'Authorization'  : authorizationToken,
                                     }, json = {'permissions' : 0, 'authorize' : True}
                   )

                   if discordAuthResp.ok:
                      if True:
                         if True:
                            medalToken  = f'{userId},{key}'
                            medalToken

                         oAuthRedirect  = discordAuthResp.json()['location']
                         oAuthRedirect

                      oAuthVerification = requests.get(oAuthRedirect)
                      oAuthVerification

                      if oAuthVerification.ok:
                         if True:
                            Color().log_success('Successfully Authenticated Account')
                            Color

                         nitroCodeResponse = requests.get(
                                             'https://medal.tv/api/social/discord/nitroCode',
                                              headers = {
                                                      'Accept'           : 'application/json',
                                                      'User-Agent'       : '%s' % (accountUserAgent),
                                                      'Medal-User-Agent' : '%s' % (accountUserAgent),
                                                      'X-Authentication' : '%s' % (medalToken),
                                              }, proxies = {
                                                         'http'  : f'http://{proxy}'  , 
                                                         'https' : f'http://{proxy}'
                                              } if proxy != None else None
                         ).json()

                         if True:
                            try:
                               Color().log_success('Nitro Code Created | %s' % (nitroCodeResponse['url']))
                               open('medal/output/nitro_codes.txt'  , 'a+').write('%s\n' % (nitroCodeResponse['url']))
                               open('medal/output/medal_tokens.txt' , 'a+').write('%s\n' % (medalToken))

                               if webhookUrl != None:
                                  self.sendWebhook(webhookUrl, accountUserAgent, medalToken, nitroCodeResponse['url'], authorizationToken)
                                  self

                               if deleteAfter == True:
                                  self.deleteAccount(accountUserAgent, userId, medalToken, proxy if proxy != None else None)
                                  self
                            except:
                               if True:
                                  try:
                                     Color().log_invalid(text = '"%s"' % (nitroCodeResponse['errorMessage']))
                                  except:
                                     Color().log_invalid(text = 'Undefinable Error')
                      else:
                         Color().log_invalid(text = 'Authentication Error')
                except Exception as E:
                   if True:
                      print(E)
                      print
                     
                   Color.log_invalid(text = 'Exception During Account Creation')
                   Color

class Menu:
      def printLogo():
          print(art.text2art('PromoCreator'))
          print
        
      def printOptions():
          print(f'[{Color().green_gratient(text = "1")}] - Promo Generator')
          print(f'[{Color().green_gratient(text = "2")}] - Token Dump')

      def getOption():
          return input('[$] > ')
        
      def startMenu():
          while True:
                if True:
                   Menu.printLogo()
                   Menu.printOptions()

                option = Menu.getOption()
                option

                if option == '1':
                   proxies_enabled = input('[@] Proxies [%sY%s/%sN%s] : ' % (colorama.Fore.LIGHTGREEN_EX, colorama.Fore.RESET, colorama.Fore.RED, colorama.Fore.RESET))
                   webhook_url     = input('[@] Webhook [%sURL%s] : ' % (colorama.Fore.RED, colorama.Fore.RESET))
                   
                   if True:
                      os.system('clear')
                      os

                   if True:
                      proxy   = None if proxies_enabled == 'N' else random.choice(open('medal/input/proxies.txt', 'r').readlines()).strip() 
                      webhook = webhook_url if webhook_url != '' else None
                     
                   for token in open('medal/input/tokens.txt', 'r').readlines():
                       Medal().createAccount(
                               authorizationToken = token.strip(), 
                               proxy      = proxy, 
                               webhookUrl = webhook
                       )

                   print('[$] Task Completed')
                   print, input('')

if __name__ == '__main__':
   Menu.startMenu()
   Menu
