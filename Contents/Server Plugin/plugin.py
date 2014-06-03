#! /usr/bin/env python # -*- coding: utf-8 -*-
####################

import jsonrpclib, sys, os, pprint, urllib2

class Plugin(indigo.PluginBase):

############## --- Indigo Plugin Methods --- ##############

    def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
        indigo.PluginBase.__init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs)
        self.debug = True

        self.commands = {
            'up': 'SendKey(270)',
            'down': 'SendKey(271)',
            'left': 'SendKey(272)',
            'right': 'SendKey(273)',
            'select': 'SendKey(256)',
            'back': 'SendKey(275)',
            'pause': 'Pause()',
            'get_percentage':'GetPercentage'
        }

	def __del__(self):
		indigo.PluginBase.__del__(self)

	def startup(self):
		self.debugLog(u"Boxee Plugin Started")

	def shutdown(self):
		self.debugLog(u"Boxee Plugin Stopping...")

############## --- Action Methods --- ##############

    def sendCommand(self, action, device):
        ip = device.pluginProps['ipaddress']
        cmd = self.commands[action.props['command']]
        url = 'http://%s:8800/xbmcCmds/xbmcHttp?command=%s' % (ip, cmd)
        urllib2.urlopen(url)
