from yowsup.layers.interface 						import YowInterfaceLayer, ProtocolEntityCallback 
from yowsup.layers.protocol_messages.protocolentities 			import TextMessageProtocolEntity 
from yowsup.layers.protocol_receipts.protocolentities 			import OutgoingReceiptProtocolEntity 
from yowsup.layers.protocol_acks.protocolentities 			import OutgoingAckProtocolEntity 
import requests 
from bs4 import BeautifulSoup
import os

message="info"
class EchoLayer(YowInterfaceLayer):
	@ProtocolEntityCallback("message")
	def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

		if True:
            		receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(),
				  'read', messageProtocolEntity.getParticipant())
                          
	    		if messageProtocolEntity.getBody().lower() == message.lower() :
				i=1
				info=""
				while i<len(list):
					info+=(list[i])
					i=i+1
				response=wikipedia.summary(str(info))
			else :
          		     response = "Please type info as (Ex: info xyz) to get Response"
           	        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        response,
                        to = messageProtocolEntity.getFrom())
		self.toLower(receipt)
          	self.toLower(outgoingMessageProtocolEntity)

		
	@ProtocolEntityCallback("receipt")
	def onReceipt(self, entity):
		ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
		self.toLower(ack)
   
