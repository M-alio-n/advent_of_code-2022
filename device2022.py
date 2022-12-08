class device:
    def __init__(self, inpt, pos = 0, type = None) -> None:
        self.__string = inpt # The program string that runs on the device
        self._pos = pos # The current position within the string
        self._type = type # The type of block starting at the current position
        self.__markers = { # All implemented marker types and their lengths
            'packet': 4,
            'message': 14
            }

    def find_next_marker(self,type=None,check_length=None):
        # check_length determines the maximal range to search for markers if None its up to the end of the program
        if not check_length:
            check_length = len(self.__string)-self._pos
        found_idx = []
        found_type = []
        if type:
            # Types that are determined by only 'unique characters'
            if type in ['packet','message']:
                for idx in range(self._pos+self.__markers[type],self._pos+check_length+1):
                    if len(set(self.__string[idx-self.__markers[type]:idx])) == self.__markers[type]:
                        #print(f'Next {type} at position {idx}.')
                        found_idx.append(idx)
                        found_type.append(type)
        else:
            for key in self.__markers:
                # Types that are determined by only 'unique characters'
                if key in ['packet','message']:
                    for idx in range(self._pos+self.__markers[key],self._pos+check_length+1):
                        if len(set(self.__string[idx-self.__markers[key]:idx])) == self.__markers[key]:
                            found_idx.append(idx)
                            found_type.append(key)
                            break
        if found_idx:
            next = found_idx.index(min(found_idx))
            # if type:
            #     print(f'Next {type} at position {found_idx[next]}.')
            # else:
            #     print(f'Next marker at position {found_idx[next]} of type {found_type[next]}.')
            return (found_idx[next], found_type[next])
        else:
            # if type:
            #     print(f'No more {type} markers found.')
            # else:
            #     print(f'No more markers found.')
            return (-1,None)

    def go2next_marker(self,type=None,check_length=None):
        pos, type = self.find_next_marker(type,check_length)
        if type:
            self._pos = pos
            self._type = type
        else:
            print(f'There are no more markers behind {self._pos}. This is the end...?')