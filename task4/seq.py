class Sequence(object):
    def __init__(self, sequence: str) -> None:
        """
        Input:
        - string : a sequence of 'A's, 'T's, 'G's, 'C's, 'U's
        
        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Create sequence attribute of Sequence class with type str           #
        # from the given string.                                              #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        self.sequence = string

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def transcribe(self) -> None:
        """
        Input: None

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Raise an error, since transrcibe method can work only with elements #
        # of DNA or RNA classes                                               #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        return error
        
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def hamming_distance(self, sequence) -> int:
        
        #######################################################################
        # TODO:                                                               #
        # First, check that attribute_name and given string have the same     #
        # length, if not raise Error.                                         #
        # If the length of strings is the same, loop over one of the strings  #
        # and count different letters.                                        #
        #######################################################################

        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.sequence2 = string2
        i=0
        mismatch=0
        if len(self.sequence) == len(self.sequence2):
            while i<len(self.attribute_name):
                if self.sequence[i] == self.sequence2[i]:
                    mismatch+=0
                else:
                    mismatch+=1
                i+=1
            return mismatch 
        else:
            return "error"
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

class DNA(Sequence):
    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'T', 'G', 'C' and their 
        corresponding amounts in attribute_name. 
        {'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
        """
        #######################################################################
        # TODO:                                                               #
        # Counting 'A's, 'T's, 'G's, 'C's either by                           #
        # looping over attribute_name or using a standard string method.      #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        self.attribute_name = string

        for nucleotide in ["A", "T", "G", "C"]:
            count = self.attribute_name.count(nucleotide)
            output_dict[nucleotide] = count
        
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def complement_dna(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'A's were changed to 'T's
        and vice versa, all 'C's changed to 'G's and vice versa
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over attribute_name with            #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        
        self.attribute_name = self.attribute_name.replace("T", "a")
        self.attribute_name = self.attribute_name.replace("A", "t")
        self.attribute_name = self.attribute_name.replace("G", "c")
        complited_DNA = self.attribute_name.replace("C", "g")
        
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'T's were changed to 'U's
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over attribute_name with            #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        return self.attribute_name.replace("U", "T")
    

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    
    
class RNA(Sequence):
    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'U', 'G', 'C' and their 
        corresponding amounts in attribute_name. 
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C}
        """
        #######################################################################
        # TODO:                                                               #
        # Counting 'A's, 'U's, 'G's, 'C's either by                           #
        # looping over attribute_name or using a standard string method.      #
        #######################################################################

        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

        output_dict = {}

        for nucleotide in ["A", "T", "G", "C"]:
            count = self.attribute_name.count(nucleotide)
            output_dict[nucleotide] = count
        
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'U's were changed to 'T's
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over attribute_name with            #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        
        return self.attribute_name.replace("U", "T")

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****