from manim import *

class AnimasiSoal1(Scene):
    def construct(self):
        a = '{'
        b = '}'
        tex = Text("Soal 1: Buatlah sebuah class template 1 parameter yang",t2c={"template":BLUE}).scale(0.5)
        tex2 = Text("\nbernama Trapezoid dan mempunyai atribut base1, base2, dan height.",t2c={"T ":TEAL,"class":ORANGE,"Trapezoid":RED}).scale(0.5).shift(DOWN*0.5)
        self.wait(2)
        text = Text("1. template<class T >",t2c={"template":BLUE}).scale(0.5).to_corner(UL)
        text2 = Text(f"\n2. \n3. class Trapezoid"+a
                    +"\n4. \tpublic:\n5. \tT base1, base2, height;\n6. "+
                    b+";",t2c={"Trapezoid":RED,"T ":TEAL,"class":ORANGE}).scale(0.5).to_corner(UL).shift(DOWN*0.5)
        self.play(Write(tex))
        self.wait(1.5)
        self.play(Write(tex2))
        self.wait(4)
        self.play(Transform(tex,text))
        self.wait(4)
        self.play(Transform(tex2,text2))
        self.wait(7)
class AnimasiSoal2(Scene):
    def construct(self):
        a = '{'
        b = '}'
        tex = Text("2. Melanjutkan class sebelumnya",color=TEAL).scale(0.5)
        tex2 = Text("Ubah atribut menjadi private",t2c={"private":PURPLE}).scale(0.5).shift(DOWN*0.5)
        tex3 = Text("Buatkan 2 konstruktor, konstruktor default yang mengisi semua atribut dengan nilai 10",t2c={"10":PURPLE}).scale(0.5).shift(DOWN)
        tex4 = Text("dan konstruktor yang mengisi nilai atribut atribut tersebut").scale(0.5).shift(DOWN*1.5)
        tex5 = Text("Lalu buat Method setter dan getter",t2c={"setter":PINK,"getter":PINK}).scale(0.5).shift(DOWN*2)
        MalasNulisUlang = [tex,tex2,tex3,tex4,tex5]
        
        text = Text("1. template<class T >",t2c={"template":BLUE}).scale(0.5).to_corner(UL)
        text1 = Text(f"\n2. \n3. class Trapezoid"+a
                    +"\n4. \tpublic:\n5. \tT base1, base2, height;\n6. "+
                    b+";",t2c={"Trapezoid":RED,"T ":TEAL,"class":ORANGE}).scale(0.5).to_corner(UL).shift(DOWN*0.5)
        text2 = Text(f"\n2. \n3. class Trapezoid"+a
                    +"\n4. \tT base1, base2, height;",t2c={"Trapezoid":RED,"T ":TEAL,"class":ORANGE}).scale(0.5).to_corner(UL).shift(DOWN*0.5)
        text3 = Text("5.\tpublic :\n6.\tTrapezoid() {\n7.\t\tbase1 = 10;base2 = 10;height = 10;\n8.\t}",t2c={"10":PURPLE,"Trapezoid":RED}).scale(0.5).to_corner(UL).shift(DOWN*1.0)
        text4 = Text("\n9.\tTrapezoid(T a, T b, T c) {\n10.\t\tbase1 = a;base2 = b;height = c;\n11.\t}",t2c={"Trapezoid":RED,"T ":TEAL}).scale(0.5).to_corner(UL).shift(DOWN*2.5)
        text5 = Text("\n12.\tvoid setBase1(T a){base1 = a;}\n13.\tvoid setBase2(T a){base2 = a;}\n14.\tvoid setHeight(T a){height= a ;}",t2c={"setBase1":PINK,"setBase2":PINK,"setHeight":PINK,}).scale(0.5).to_corner(UL).shift(DOWN*3.5)
        text6 = Text("\n15.\tT getBase1(){return base1;}\n16.\tT getBase2(){return base2;}\n17.\tT getHeight(){return height;}\n18.};",t2c={"getBase1":PINK,"getBase2":PINK,"getHeight":PINK}).scale(0.5).to_corner(UL).shift(DOWN*4.5)
        full1 = VGroup(text,text1)
        full2 = VGroup(text,text2)
        full3 = VGroup(text5,text6)
        for i in MalasNulisUlang:
            Timing = len(i)/30
            self.play(Write(i),lag_ratio=Timing)
        self.wait(5)
        self.play(ReplacementTransform(tex,full1))
        self.wait(3)
        self.play(ReplacementTransform(full1,full2))
        self.play(tex2.animate.to_corner(UL).shift(DOWN*0.5),FadeOut(tex2))
        self.wait(2)
        self.play(ReplacementTransform(tex3,text3))
        self.play(ReplacementTransform(tex4,text4))
        self.wait(3)
        self.play(ReplacementTransform(tex5,full3))
        self.wait(4)        
class AnimasiSoal3(Scene):
    def construct(self):
        tex = Text("Soal 3. Masih menggunakan class sebelumnya",color=BLUE)
        tex1 = Text("Buat method calculateArea() yang menghitung luas Trapezoid.",t2c={"calculateArea":GREEN})
        tex2 = Text("Lalu buat method calculatePerimeter() yang menghitung keliling Trapezoid",t2c={"calculatePerimeter":GREEN})
        full = VGroup(tex,tex1,tex2).scale(0.5).arrange(DOWN*0.5)