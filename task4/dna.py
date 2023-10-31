class DNA(object):
    def __init__(self, string : str) -> None:
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.attribute_name = string

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def count_nucleotides(self) -> dict:
     # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        output_dict = {}

        for nucleotide in ["A", "T", "G", "C"]:
            count = self.attribute_name.count(nucleotide)
            output_dict[nucleotide] = count

        return output_dict
       # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def transcribe(self) -> str:
       
        return self.attribute_name.replace("T", "U")
        
      # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def complement_dna(self) -> str:
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.attribute_name = self.attribute_name.replace("T", "a")
        self.attribute_name = self.attribute_name.replace("A", "t")
        self.attribute_name = self.attribute_name.replace("G", "c")
        complited_DNA = self.attribute_name.replace("C", "g")
    
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****


    def hamming_distance(self, string2 : str) -> int:
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.attribute_name2 = string2
        i=0
        mismatch=0
        if len(self.attribute_name) == len(self.attribute_name2):
            while i<len(self.attribute_name):
                if self.attribute_name[i] == self.attribute_name2[i]:
                    mismatch+=0
                else:
                    mismatch+=1
                i+=1
        else:
            return "error"
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****


class RNA(object):
    def __init__(self, string : str) -> None:
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.attribute_name = string
        
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> str:
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return self.attribute_name.replace("U", "T")
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        