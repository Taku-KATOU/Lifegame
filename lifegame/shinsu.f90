program shinsu
  implicit none
  integer :: n
  integer :: a(8),j

  !do i=0,255
  n=54
  j=1
  a=0
  do while(n>0)
     a(9-j)=mod(n,2)
     n=n/2
     j=j+1
  end do
  write(*,*)a(1:8)
  write(*,*)sum(a)
  stop
end program shinsu
  !end do
