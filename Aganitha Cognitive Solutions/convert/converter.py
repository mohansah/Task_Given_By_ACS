class converter:
    def convertParagraph(self,st):
        st = st.replace("two dollars","$2")
        st = st.replace("C M","CM")
        st = st.replace("Triple A","AAA")
        st = st.replace("United State of America","USA")
        return st