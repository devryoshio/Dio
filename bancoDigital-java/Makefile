
JFLAGS = -g
JC = javac
JVM =  java
RM =rm -rf

CLASSES = \
        Banco.java \
        Cliente.java \
        Conta.java \
        ContaCorrente.java \
        ContaPoupanca.java \
        IConta.java \
        Main.java 


.SUFFIXES: .java .class

.java.class:
	$(JC) $(JFLAGS) $*.java

#nome da classe que contem main 
MAIN = Main

run: $(MAIN).class
	$(JVM) $(MAIN) $(FILE)




default: classes


clean:
	$(RM) *.class
