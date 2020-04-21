
# bug



# routing

Getting around the useless Virgin Media Business' routers ability to only port foward to the same port:

```
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 5000
iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 5000
```

# certbot

```sudo certbot certonly --manual --preferred-challenges dns```

 - Congratulations! Your certificate and chain have been saved at:            
   /etc/letsencrypt/live/qwazzock-dev.randall.lol/fullchain.pem               
   Your key file has been saved at:                             
   /etc/letsencrypt/live/qwazzock-dev.randall.lol/privkey.pem                
   Your cert will expire on 2020-07-19. To obtain a new or tweaked            
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew" 