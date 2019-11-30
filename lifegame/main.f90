program main
  use const
  use life
  use init
  implicit none
  integer :: lif(m,n),env(0:m+1,0:n+1),fate(0:255,0:1),newlif(m,n)
  integer :: i,j
  character(len=4) :: a
  character(len=*),parameter :: dir="./dat/"
  !determine fate
  call dead_or_alive(fate)
  !open(10,file="destiny.dat")
  !do i=0,255
  !   write(10,*)fate(i,0:1)
  !end do
  close(10)
  !set init_life
  call init_life(lif)
  do j=0,nmax
     !call nextlife(lif,newlif,env,fate)
     !lif=newlif
     !output file
     write(a,'(i4.4)')j
     !write(*,*)dir
     !write(*,*)dir//a//"data.dat"
     open(10,file=dir//"data"//a//".dat")
     do i=1,m
        write(10,*)lif(i,1:n)
     end do
     close(10)
     call nextlife(lif,newlif,env,fate)
     lif=newlif
  end do


  
  stop
end program main

  
