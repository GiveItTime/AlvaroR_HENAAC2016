;======================================================================
; Name: Alvaro Rivas
; Date: 5/12/2016
; Version: MS 2012
; Description:
;	Program computes a three by three matrix multiplication problem
;	and displays the answer.
;======================================================================
INCLUDE Irvine32.inc

.data
row1Array BYTE 1, 3, -4
row2Array BYTE 1, 1, -2
row3Array BYTE -1, -2, 5
column1Array BYTE 8, 3, 0
column2Array BYTE 3, 10, 2
column3Array BYTE 0, 2, 6

sum WORD ?
temp BYTE ?
spaceString Byte '	'

.code
main PROC
	mov ecx, 3
	mov esi, 0
	mov sum, 0
L1:
	mov al,row1Array[esi]
	
	mov bl, column1Array[esi]
	
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L1
	movsx eax, sum
	

	call WriteDec
	mov edx, OFFSET spaceString
	call WriteString

	mov ecx, 3
	mov esi, 0
	mov sum, 0
L2:
	mov al,row1Array[esi]
	mov bl, column2Array[esi]
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L2
	movzx eax, sum
	call WriteDec 
	mov edx, OFFSET spaceString
	call WriteString
	
	mov ecx, 3
	mov esi, 0
	mov sum, 0
L3:
	mov al,row1Array[esi]
	mov bl, column3Array[esi]
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L3
	movsx eax, sum	
	call WriteInt 
	mov edx, OFFSET spaceString
	call WriteString	
	call CRLF
	
	mov ecx, 3
	mov esi, 0
	mov sum, 0
L4:
	mov al,row2Array[esi]
	mov bl, column1Array[esi]
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L4
	movzx eax, sum
	call WriteDec 
	mov edx, OFFSET spaceString
	call WriteString

	mov ecx, 3
	mov esi, 0
	mov sum, 0
L5:
	mov al,row2Array[esi]
	mov bl, column2Array[esi]
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L5
	movzx eax, sum
	call WriteDec 
	mov edx, OFFSET spaceString
	call WriteString
	
	mov ecx, 3
	mov esi, 0
	mov sum, 0
L6:
	mov al,row2Array[esi]
	mov bl, column3Array[esi]
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L6
	movsx eax, sum
	
	call WriteInt
	mov edx, OFFSET spaceString
	call WriteString
	call CRLF

	mov ecx, 3
	mov esi, 0
	mov sum, 0
L7:
	mov al,row3Array[esi]
	mov bl, column1Array[esi]
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L7
	movsx eax, sum
	call WriteInt 
	mov edx, OFFSET spaceString
	call WriteString

	mov ecx, 3
	mov esi, 0
	mov sum, 0
L8:
	mov al,row3Array[esi]
	mov bl, column2Array[esi]
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L8
	movsx eax, sum
	call WriteInt 
	mov edx, OFFSET spaceString
	call WriteString
	
	mov ecx, 3
	mov esi, 0
	mov sum, 0
L9:
	mov al,row3Array[esi]
	mov bl, column3Array[esi]
	imul bl
	
	add sum, ax ; multi ans
	
	inc esi
loop L9
	movzx eax, sum
	
	call WriteDec 
	mov edx, OFFSET spaceString
	call WriteString
	call CRLF
	Call waitmsg
	

	exit
main ENDP
END main