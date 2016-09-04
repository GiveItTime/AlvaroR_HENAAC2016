;================================================================================================================
; Name: Alvaro Rivas
; Date: 3/17/2016
; Version: MS 2012
; Description:
;	Program uses Push and Pop to reverses the elements of the array dwarray and displays them in reverse order.
;================================================================================================================
INCLUDE Irvine32.inc

.data
dwarray DWORD 3, 5, 7 , 9, 13, 15, 17, 19 

.code
main PROC
    mov     ecx, 8
    mov     esi, 0

L1:	push    dwarray[esi]   
    add     esi, 4      ; add 4 to dwarray pointer
    loop    L1          ; loop until ecx == 0

	mov     ecx, 8      ; reset loop counter
	mov		esi, 0

L2:	pop		eax
	mov dwarray[esi],eax
    add esi,4
    loop L2

	mov esi, OFFSET dwarray
 	mov ecx, LENGTHOF dwarray
	mov ebx, TYPE dwarray
    call DumpMem
	call WaitMsg
    exit
main ENDP
END main
	