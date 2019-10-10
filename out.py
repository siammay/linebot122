# uncompyle6 version 3.4.1
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.16 (default, Jul 28 2019, 22:06:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: loginme.py
# Size of source mod 2**32: 8278 bytes
from MIGHTAPI.MIGHTLY import LINE, OEPoll
from Naked.toolshed.shell import execute_js
import multiprocessing
from akad.ttypes import TalkException as TalkE
from multiprocessing import Process
from akad.ttypes import TalkException
import livejson, traceback, sys
app = 'WIN10\t5.9.0\tSpamJS\t12'
appJS = 'DESKTOPMAC\t5.11.1\tSpamJS\t12'
settings = livejson.File('settings_f.json')
proc = []
if 'token' not in settings:
    settings['token'] = '#'
if 'contact' not in settings:
    settings['contact'] = []
if 'name' not in settings:
    settings['name'] = u'@\u026a\u0274\u1d20\u026a\u1d1b\u1d07\u1d07:\u1786\u17b6\u0e38\u0c10\u09a3\u0beb\u09a3\u0c10'
exg = LINE(appName=appJS)
cPoll = OEPoll(exg)
set = {'get':False,  'remove':False}

def runadd(uid):
    return execute_js(f"spamadd.js uid={uid}")


def start_run(to, contacts=settings['contact']):
    if contacts == []:
        return False
    try:
        client = LINE(_to=to, _client=exg, appName=appJS)
    except:
        exg.sendMessage(to, u'\u0e25\u0e47\u0e2d\u0e01\u0e2d\u0e34\u0e19\u0e44\u0e21\u0e48\u0e2a\u0e4d\u0e32\u0e40\u0e23\u0e47\u0e08')
        return False
    else:
        if client.getSettings().e2eeEnable == True:
            client.sendMessage(to, u'\u0e01\u0e23\u0e38\u0e13\u0e32\u0e1b\u0e34\u0e14 Letter Sealing \u0e01\u0e48\u0e2d\u0e19\u0e17\u0e4d\u0e32\u0e01\u0e32\u0e23\u0e23\u0e31\u0e19')
            return False
        cmd = 'spam.js token={} mid={} name={}'.format(client.authToken, client.profile.mid, settings['name'].strip())
        parsed_list = [c.mid for c in client.getContacts(contacts)]
        friends = client.getAllContactIds()
        for mid in parsed_list:
            if mid not in friends:
                try:
                    client.findAndAddContactsByMid(mid)
                except:
                    try:
                        client.sendMessage(to, 'Unable to add contact. {}'.format(mid))
                    except TalkE as err:
                        try:
                            if err.code in (7, 8, 20):
                                return exg.sendMessage(to, u'\u0e01\u0e23\u0e38\u0e13\u0e32\u0e25\u0e47\u0e2d\u0e01\u0e2d\u0e34\u0e19\u0e43\u0e2b\u0e21\u0e48\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07')
                        finally:
                            err = None
                            del err

                cmd += ' uid={}'.format(mid)

        execute_js(cmd)
        exg.sendMessage(to, '[@invitee:NOTIF]\nDone operation.')


help = u'\u0e04\u0e4d\u0e32\u0e2a\u0e31\u0e48\u0e07\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14\u0e02\u0e2d\u0e07 @INVITEE #Beta\n@invitee:help\n@invitee:contact ~ \u0e40\u0e0a\u0e47\u0e04\u0e04\u0e17.\n@invitee:getmode ~ \u0e40\u0e1b\u0e34\u0e14/\u0e1b\u0e34\u0e14\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e04\u0e2d\u0e19\u0e41\u0e17\u0e04\n@invitee:removemode ~ \u0e40\u0e1b\u0e34\u0e14/\u0e1b\u0e34\u0e14\u0e01\u0e32\u0e23\u0e25\u0e1a\u0e04\u0e2d\u0e19\u0e41\u0e17\u0e04\n@invitee:check [\u0e40\u0e25\u0e02] ~ \u0e40\u0e0a\u0e47\u0e04\u0e04\u0e17.\u0e43\u0e19\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\n@invitee:remove [\u0e40\u0e25\u0e02] ~ \u0e25\u0e1a\u0e04\u0e17.\u0e43\u0e19\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\n@invitee:runadd [\u0e40\u0e25\u0e02] ~ \u0e23\u0e31\u0e19\u0e41\u0e2d\u0e14\u0e04\u0e17.\u0e43\u0e19\u0e23\u0e32\u0e22\u0e0a\u0e37\u0e48\u0e2d\n@invitee:setname [\u0e0a\u0e37\u0e48\u0e2d\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23] ~ \u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e49\u0e2d\u0e07\u0e23\u0e31\u0e19\n@invitee:login ~ \u0e25\u0e47\u0e2d\u0e01\u0e2d\u0e34\u0e19\n*** \u0e40\u0e21\u0e37\u0e48\u0e2d\u0e25\u0e1a\u0e41\u0e25\u0e49\u0e27 \u0e08\u0e30\u0e17\u0e4d\u0e32\u0e43\u0e2b\u0e49\u0e40\u0e25\u0e02\u0e04\u0e25\u0e32\u0e14\u0e40\u0e04\u0e25\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e14\u0e49 \u0e01\u0e23\u0e38\u0e13\u0e32\u0e40\u0e0a\u0e47\u0e04\u0e40\u0e25\u0e02\u0e2d\u0e35\u0e01\u0e04\u0e23\u0e31\u0e49\u0e07*** '

def operator(op):
    msg = op.message
    if msg.contentType not in (0, 13):
        return
    if msg.toType != 2:
        return
    if msg.contentType == 0:
        mlow = msg.text.lower()
        if mlow == '@invitee:contact':
            if settings['contact'] == []:
                return
            no = 0
            del_list = []
            for mid in settings['contact']:
                try:
                    exg.getContact(mid)
                except:
                    del_list.append(mid)

            for d in del_list:
                settings['contact'].remove(d)

            if del_list != []:
                exg.sendMessage(msg.to, u'\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e25\u0e1a\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e08\u0e4d\u0e32\u0e19\u0e27\u0e19 {} \u0e04\u0e19'.format(str(len(del_list))))
            stry = u'\u0e1a\u0e31\u0e0d\u0e0a\u0e35\u0e17\u0e35\u0e48\u0e23\u0e31\u0e19:\n'
            for name in [m.displayName for m in exg.getContacts(settings['contact'])]:
                no = no + 1
                stry += '{}. {}\n'.format(str(no), name)

            exg.sendMessage(msg.to, stry[:-1])
        elif mlow == '@invitee:login':
            start_run(msg.to)
        elif mlow == '@invitee:help':
            exg.sendMessage(msg.to, help)
        elif mlow.startswith('@invitee:runadd '):
            split = msg.text.split(' ')[1]
            try:
                split = int(split)
            except:
                return exg.sendMessage(msg.to, u'\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19')
            else:
                try:
                    s = settings['contact'][(split - 1)]
                except:
                    return exg.sendMessage(msg.to, u'\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e04\u0e17.\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e08\u0e30\u0e23\u0e31\u0e19\u0e41\u0e2d\u0e14')
                else:
                    contact = settings['contact'][(split - 1)]
                    runadd(contact)
                    exg.sendMessage(msg.to, u'\u0e40\u0e23\u0e35\u0e22\u0e1a\u0e23\u0e49\u0e2d\u0e22')
        elif mlow.startswith('@invitee:remove '):
            split = msg.text.split(' ')[1]
            try:
                split = int(split)
            except:
                return exg.sendMessage(msg.to, u'\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19')
            else:
                try:
                    s = settings['contact'][(split - 1)]
                except:
                    return exg.sendMessage(msg.to, u'\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e04\u0e17.\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e08\u0e30\u0e25\u0e1a')
                else:
                    name = exg.getContact(settings['contact'][(split - 1)]).displayName
                    settings['contact'].remove(settings['contact'][(split - 1)])
                    exg.sendMessage(msg.to, u'\u0e25\u0e1a\u0e04\u0e17.\u0e0a\u0e37\u0e48\u0e2d {} \u0e2d\u0e2d\u0e01\u0e41\u0e25\u0e49\u0e27!'.format(name))
        elif mlow.startswith('@invitee:check '):
            split = msg.text.split(' ')[1]
            try:
                split = int(split)
            except:
                return exg.sendMessage(msg.to, u'\u0e15\u0e31\u0e27\u0e40\u0e25\u0e02\u0e40\u0e17\u0e48\u0e32\u0e19\u0e31\u0e49\u0e19')
            else:
                try:
                    s = settings['contact'][(split - 1)]
                except:
                    return exg.sendMessage(msg.to, u'\u0e44\u0e21\u0e48\u0e1e\u0e1a\u0e04\u0e17.\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23')
                else:
                    name = settings['contact'][(split - 1)]
                    exg.sendContact(msg.to, name)
        elif mlow.startswith('@invitee:setname '):
            name = msg.text.split(' ')[1].strip()
            if len(name) >= 50:
                exg.sendMessage(msg.to, u'\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e49\u0e2d\u0e07\u0e22\u0e32\u0e27\u0e40\u0e01\u0e34\u0e19\u0e44\u0e1b')
                return
            settings['name'] = name
            exg.sendMessage(msg.to, u'\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e49\u0e2d\u0e07\u0e23\u0e31\u0e19\u0e40\u0e1b\u0e47\u0e19 {} \u0e41\u0e25\u0e49\u0e27!'.format(settings['name']))
    if mlow == '@invitee:getmode':
        set['get'] = True if not set['get'] else False
        set['remove'] = False
        if set['get']:
            exg.sendMessage(msg.to, u'\u0e40\u0e1b\u0e34\u0e14\u0e23\u0e31\u0e1a\u0e04\u0e2d\u0e19\u0e41\u0e17\u0e04\u0e41\u0e25\u0e49\u0e27!')
        else:
            exg.sendMessage(msg.to, u'\u0e1b\u0e34\u0e14\u0e23\u0e31\u0e1a\u0e04\u0e2d\u0e19\u0e41\u0e17\u0e04\u0e41\u0e25\u0e49\u0e27')
    elif mlow == '@invitee:removemode':
        set['remove'] = True if not set['remove'] else False
        set['get'] = False
        if set['remove']:
            exg.sendMessage(msg.to, u'\u0e40\u0e1b\u0e34\u0e14\u0e22\u0e01\u0e40\u0e25\u0e34\u0e01\u0e04\u0e2d\u0e19\u0e41\u0e17\u0e04\u0e41\u0e25\u0e49\u0e27')
        else:
            exg.sendMessage(msg.to, u'\u0e1b\u0e34\u0e14\u0e22\u0e01\u0e40\u0e25\u0e34\u0e01\u0e04\u0e2d\u0e19\u0e41\u0e17\u0e04\u0e41\u0e25\u0e49\u0e27')
    else:
        if msg.contentType == 13:
            pass

    if set['get']:
        if msg.contentMetadata['mid'] not in settings['contact']:
            settings['contact'].append(msg.contentMetadata['mid'])
            exg.sendMessage(msg.to, u'\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e41\u0e25\u0e49\u0e27')
        if set['remove']:
            pass
    if msg.contentMetadata['mid'] in settings['contact']:
        settings['contact'].remove(msg.contentMetadata['mid'])
        exg.sendMessage(msg.to, u'\u0e25\u0e1a\u0e2d\u0e2d\u0e01\u0e40\u0e23\u0e35\u0e22\u0e1a\u0e23\u0e49\u0e2d\u0e22\u0e41\u0e25\u0e49\u0e27')


def start():
    while True:
        try:
            ops = ''
            try:
                ops = cPoll.singleTrace(count=50)
            except Exception as e:
                try:
                    print('[TRACING ERR] {}'.format(e))
                    return
                finally:
                    e = None
                    del e

            for op in ops:
                if op.type in (25, 26):
                    try:
                        operator(op)
                    except:
                        traceback.print_exc()

                    cPoll.setRevision(op.revision)

        except Exception:
            traceback.print_exc()
        except KeyboardInterrupt:
            sys.exit(1)


if __name__ == '__main__':
    start()
# okay decompiling loginme.pyc
