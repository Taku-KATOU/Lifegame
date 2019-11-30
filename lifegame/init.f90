module init
  implicit none
  public :: dead_or_alive,init_life

contains
  subroutine dead_or_alive(fate)
    implicit none
    integer,intent(out) :: fate(0:255,0:1)
    integer :: i,j,k,a(8),b,c(3),n

    !fate=0
    !determine fate
    do i=0,255
       n=i
       j=1
       a=0
       !2shinsu-ka
       do while(n>0)
          a(9-j)=mod(n,2)
          n=n/2
          j=j+1
       end do
       b=sum(a)
       !2shinsu-ka
       n=b
       j=1
       c=0
       do while(n>0)
          c(4-j)=mod(n,2)
          n=n/2
          j=j+1
       end do
       !fate for dead
       fate(i,0)=c(2)*c(3)*(-c(1)+1)
       !fate for alive
       fate(i,1)=(-c(1)+1)*c(2)
    end do
    do i=1,256
       write(*,*)i-1,fate(i-1,0:1)
    end do
  end subroutine dead_or_alive

  subroutine init_life(life)
    use const
    implicit none
    integer,intent(inout) :: life(m,n)

    life=0
    !glider
    life(1,1)=1
    life(2,2)=1
    life(2,3)=1
    life(3,1)=1
    life(3,2)=1
  end subroutine init_life
end module init
