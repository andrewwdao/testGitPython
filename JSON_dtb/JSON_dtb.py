"""------------------------------------------------------------*-
  JSON database for Raspberry Pi
  Tested on: Raspberry Pi 3 B+
  (c) Minh-An Dao 2019
  (c) Nhat-Khoa Phan 2019
  version 1.00 - 10/10/2019
 --------------------------------------------------------------
 *
 *
 --------------------------------------------------------------"""
import json
import objcrypt

# ---------------------------- Private Parameters:
# -----Private key and CBC:
AUTH_KEY = 'minhan7497'
AUTH_CBC = 'MIS_LOCKER'


class Database:
    def __init__(self):
        self.crypter = objcrypt.Crypter(AUTH_KEY, AUTH_CBC)
        with open('database.json', 'r') as inputFile:
            self.enc_dtb = json.load(inputFile)
        self.dec_dtb = self.crypter.decrypt_object(self.enc_dtb)
        self.admin = self.dec_dtb['admin']
        self.member = self.dec_dtb['member']
        self.number_of_admin = len(self.admin)
        self.number_of_member = len(self.member)

    def update(self):
        self.enc_dtb = self.crypter.encrypt_object(self.dec_dtb)
        with open('database.json', 'w') as outputFile:
            json.dump(self.enc_dtb, outputFile)

    def addAdmin(self, rfid):
        self.admin.append({
            'rfid': rfid
        })
        self.number_of_admin += 1
        self.update()

    def delAdmin(self, rfid):
        for counter in range(0, self.number_of_admin):
            if self.admin[counter]['rfid'] == rfid:
                del self.admin[counter]
                self.number_of_admin -= 1
                self.update()
                return

    def delAllAdmin(self):
        if self.number_of_admin:
            del self.admin[0]
            self.number_of_admin -= 1
            self.delAllAdmin()
        self.update()

    def addMember(self, name, mssv, rfid, fingerNum):
        self.member.append({
            'name': name,
            'mssv': mssv,
            'rfid': rfid,
            'fing': fingerNum
        })
        self.number_of_member += 1
        self.update()

    def delMember(self, mssv):
        for counter in range(0, self.number_of_member):
            if self.member[counter]['mssv'] == mssv:
                del self.member[counter]
                self.number_of_member -= 1
                self.update()
                return

    def delAllMember(self):
        if self.number_of_member:
            del self.member[0]
            self.number_of_member -= 1
            self.delAllMember()
        self.update()

    def searchAdmin(self, rfid):
        for counter in range(0, self.number_of_admin):
            if self.admin[counter]['rfid'] == rfid:
                return [True, counter]
        return [False, 9999]

    def searchRFID(self, rfid):
        for counter in range(0, self.number_of_member):
            if self.member[counter]['rfid'] == rfid:
                return [True, counter]
        return [False, 9999]

    def changeRFID(self, mssv, rfid):
        for counter in range(0, self.number_of_member):
            if self.member[counter]['mssv'] == mssv:
                self.member[counter]['rfid'] = rfid
                self.update()
                return True
        return False

    def searchFinger(self, fingerNum):
        for counter in range(0, self.number_of_member):
            if self.member[counter]['fing'] == fingerNum:
                return [True, counter]
        return [False, 9999]

    def changeFinger(self, mssv, fingerNum):
        for counter in range(0, self.number_of_member):
            if self.member[counter]['mssv'] == mssv:
                self.member[counter]['fing'] = fingerNum
                self.update()
                return True
        return False

    def getInfo(self, memberNum):
        return [self.member[memberNum]['name'], self.member[memberNum]['mssv']]

