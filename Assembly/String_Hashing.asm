;======================================================================
; Name: Alvaro Rivas
; Date: 4/21/2016
; Version: MS 2012
; Description:
;	Program hashes ten string arrays using hashing algorithm and displays 
;	the string along with the corresponding hash value.
;======================================================================
INCLUDE Irvine32.inc

TABLE_SIZE = 13

.data
; Strings to be Hashed
str1 BYTE "Herman Smith", 0
str2 BYTE "Louie Jones", 0
str3 BYTE "Robert Sherman", 0
str4 BYTE "Barbara Goldenstein", 0
str5 BYTE "Johnny Unitas", 0
str6 BYTE "Tyler Abrams", 0
str7 BYTE "April Perkins", 0
str8 BYTE "William Jones", 0
str9 BYTE "Steve Schokley", 0
str10 BYTE "Steve Williams", 0

hashV BYTE " Hash Value = ",0
temp Byte ?
.code
main	PROC
		
		mov ecx, LENGTHOF str1 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str1 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str2 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str2 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str3 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str3 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str4 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str4 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str5 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str5 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str6 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str6 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str7 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str7 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str8 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str8 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str9 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str9 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF

		mov ecx, LENGTHOF str10 - 1 ; move length of string into ecx register for loop
		mov edi, OFFSET str10 ; move string into edi register
		call HashFunction ; Hashing Function
		mov edx, OFFSET hashV
		call WriteString
		movzx eax, temp
		call WriteDec ; Displays Remainder
		call CRLF
		call WaitMsg
		exit
main ENDP

; Hashes a string
HashFunction PROC
	
	mov al, 0
; loops through string
L1:
		mov al, [edi] 
		call WriteChar

		; reduces number of collisions
		rcl al, 5 
		xor al, 00110010b
		add al, [edi]
		
		mov temp, al
		inc edi ; increments loop
	loop L1
	movzx ax, temp
	mov bl, TABLE_SIZE		; TABLE_SIZE = 13
	idiv bl					; Divides Sum
	mov temp, ah			; stores remainder

	ret
HashFunction ENDP

END main