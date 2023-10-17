def create_po (po_nu, port_list, mode = 'active', vpc_peer_link = 0, vpc_id = 0, switchport = 0, make_int_default = 1):
   conf_str = ""
   match = re.search(r'(\d+)', str(po_nu))
   po_nu = match.group(1)
   for port1 in port_list:
     if make_int_default:
        conf_str += 'default interface ' + port1 + '\n' 
     conf_str += 'interface ' + port1 + '\n'
     conf_str += 'load-interval counter 1 30 \n'
     conf_str += 'load-interval counter 2 300 \n'
     conf_str += 'no shut \n'
     if mode == 'static':
        conf_str += 'channel-group ' + str(po_nu) + '\n'
     else:
        conf_str += 'channel-group ' + str(po_nu) + ' mode ' + mode + '\n'
   if switchport:
      conf_str += 'interface port-channel ' + str(po_nu) + '\n'
      conf_str += 'switchport\n'
   if vpc_peer_link:
      conf_str += 'interface port-channel ' + str(po_nu) + '\n'
      conf_str += 'switchport\n'
      conf_str += 'vpc peer-link\n'
   if vpc_id:
      conf_str += 'interface port-channel ' + str(po_nu) + '\n'
      conf_str += 'vpc ' + str(vpc_id) + '\n'

   return conf_str
