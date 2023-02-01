# Successfull Attempt

# Note: 1. I change file name of user_email_hash.1m.tsv to user_email_hash_1m.tsv
#       2. I add cloumn header on plain_32m.tsv file because it hasn't had any common connection between other files.
#       3. I try to write minimum processing script because my laptop aren't coprating with me.
#       4. ignore warnings because data is not purify 


# pandas lib

import pandas as pd


# reading data

tsv1 = pd.read_csv("./user_email_hash_1m.tsv", sep='\t')
tsv2 = pd.read_csv("./ip_1m.tsv", sep='\t')
tsv3 = pd.read_csv("./plain_32m.tsv", sep='\t')

# Merging two file with same or common value i.e ID and stored data in part_1

output_dataFrame_part_1 = pd.merge(tsv1, tsv2, on='id', how='inner')

# And again merging last file with new output file and both have common value to merge

output_dataFrame_part_2 = pd.merge(output_dataFrame_part_1, tsv3, on='email', how='inner')


# Writing output data in output.tsv file

output_dataFrame_part_2.to_csv("./output.tsv", sep='\t', header=True, index=False)


#############################################################################################################################

# ATTEMPT NO: 01 [PARTIAL CORRECT]


# #reading data
# r_ip_data = 'ip_1m.tsv'
# r_id_user_email_hash = './user_email_hash_1m.tsv'
# r_plain_password='plain_32m.tsv'


# #writing output data
# w_output = 'output.tsv'


# file_read = pd.read_csv(r_id_user_email_hash,sep= '\t')

# print(file_read.head(10));


# #write in output file

# with open(w_output,'w') as write_tsv:
#     write_tsv.write(file_read.to_csv(sep=',',index=False))

################################################################################################################################

# ATTEMPT NO: 02 [FAILED]


# from glob import glob

# filename= 'output.tsv'

# with open(filename,'a') as singleFile:
#     first_tsv = True
#     for tsv in glob('*.tsv'):
#         if tsv == filename:
#             pass
#         else:
#             header = True
#             for line in open(tsv, 'r'):
#                 if first_tsv and header:
#                     singleFile.write(line)
#                     first_tsv = False
#                     header= False
#                 elif header:
#                     header=False
#                 else:
#                     singleFile.write(line)
#     singleFile.close()


############################################################################################################################

# ATTEMPT NO: 03


# import pandas as pd
# import glob

# path = './data'
# tsvfiles = glob.glob(path + "/*.tsv")
# for t in tsvfiles:
#     tsv = pd.read_table(t, sep='\t')
#     tsv.to_csv(t[:-4] + '.csv', index=False)
