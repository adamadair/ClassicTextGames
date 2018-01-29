def intro():
    print(tab(34) + "LEM")
    print(tab(15) + "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")


def tab(t):
    return " " * t


class Rockt2:
    """
    ROCKT2 IS AN INTERACTIVE GAME THAT SIMULATES A LUNAR
    LANDING IS SIMILAR TO THAT OF THE APOLLO PROGRAM.
    THERE IS ABSOLUTELY NO CHANCE INVOLVED
    """

    def __init__(self):
        self.Z = 6080
        self.M_STR = "FEET"
        self.G3 = 0.592
        self.N_STR = "N.MILES"
        self.G5 = 1000
        self.Z_STR = "GO"
        self.B1 = 1
        self.M = 17.95
        self.F1 = 5.25
        self.N = 7.5
        self.R0 = 926
        self.V0 = 1.29
        self.T = 0
        self.H0 = 60
        self.R = self.R0 + self.H0
        self.A = -3.425
        self.R1 = 0
        self.A1 = 8.84361E-04
        self.R3 = 0
        self.A3 = 0
        self.M1 = 7.45
        self.M0 = self.M1
        self.B = 750
        self.T1 = 0
        self.F = 0
        self.P = 0
        self.N = 1
        self.M2 = 0
        self.S = 0
        self.C = 0
        self.K = -1

    def user_choice(self, prompt, choices):
        resp = ""
        c = [str(x).lower() for x in choices]
        while resp not in c:
            resp = input(prompt).lower()
            if resp not in choices:
                print("JUST ANSWER THE QUESTION, PLEASE, ")
        return resp

    def instructions(self, q):
        """
        print instructions. lines 315-480
        """
        if q[0] != 'y':
            print("\n  YOU ARE ON A LUNAR LANDING MISSION.  AS THE PILOT OF")
            print("THE LUNAR EXCURSION MODULE, YOU WILL BE EXPECTED TO")
            print("GIVE CERTAIN COMMANDS TO THE MODULE NAVIGATION SYSTEM.")
            print("THE ON-BOARD COMPUTER WILL GIVE A RUNNING ACCOUNT")
            print("OF INFORMATION NEEDED TO NAVIGATE THE SHIP.\n\n")  # line 8
            print("THE ATTITUDE ANGLE CALLED FOR IS DESCRIBED AS FOLLOWS.")
            print("+ OR -180 DEGREES IS DIRECTLY AWAY FROM THE MOON")
            print("-90 DEGREES IS ON A TANGENT IN THE DIRECTION OF ORBIT")
            print("+90 DEGREES IS ON A TANGENT FROM THE DIRECTION OF ORBIT")
            print("0 (ZERO) DEGREES IS DIRECTLY TOWARD THE MOON\n")  # line 16
            print(tab(30) + "-180|+180")
            print(tab(34) + "^")
            print(tab(27) + "-90 < -+- > +90")
            print(tab(34) + "!")
            print(tab(34) + "0")
            print(tab(21) + "<<<< DIRECTION OF ORBIT <<<<\n")
            print(tab(20) + "------ SURFACE OF MOON ------ \n")
            print("ALL ANGLES BETWEEN -180 AND +180 DEGREES ARE ACCEPTED.")
            input("<press enter>")
            print("1 FUEL UNIT = 1 SEC. AT MAX THRUST")
            print("ANY DISCREPANCIES ARE ACCOUNTED FOR IN THE USE OF FUEL")
            print("FOR AN ATTITUDE CHANGE.")
            print("AVAILABLE ENGINE POWER: 0 (ZERO) AND ANY VALUE BETWEEN")
            print("10 AND 100 PERCENT.\n")
            print("NEGATIVE THRUST OR TIME IS PROHIBITED.\n")

        print("\nINPUT: TIME INTERVAL IN SECONDS ------ (T)")
        print("       PERCENTAGE OF THRUST ---------- (P)")
        print("       ATTITUDE ANGLE IN DEGREES ----- (A)\n")

        if q[0] != 'y':
            print("FOR EXAMPLE:")
            print("T,P,A? 10,65,-60")
            print("TO ABORT THE MISSION AT ANY TIME, ENTER 0,0,0\n")

        print("OUTPUT: TOTAL TIME IN ELAPSED SECONDS")
        print("        HEIGHT IN " + self.M_STR)
        print("        DISTANCE FROM LANDING SITE IN " + self.M_STR)
        print("        VERTICAL VELOCITY IN " + self.M_STR + "/SECOND")
        print("        HORIZONTAL VELOCITY IN " + self.M_STR + "/SECOND")
        print("        FUEL UNITS REMAINING\n")

    def run(self):
        intro()
        q = self.user_choice("HAVE YOU FLOWN AN APOLLO/LEM MISSION BEFORE (YES OR NO)? ", ["yes", "no"])
        self.K = self.get_measurement_option(q)
        if self.K == 0:
            self.Z = 6080
            self.M_STR = "FEET"
            self.G3 = 0.592
            self.N_STR = "N.MILES"
            self.G5 = 1000
        else:
            self.Z = 1852.8
            self.M_STR = "METERS"
            self.G3 = 3.6
            self.N_STR = " KILOMETERS"
            self.G5 = 1000
        self.instructions(q)

        # for i in range(self.n - 1):
        #    if self.M1 != 0:


    def get_measurement_option(self, q):
        i = -1
        if q == 'yes':
            m = input("INPUT MEASUREMENT OPTION NUMBER? ")
            try:
                i = int(m)
            except:
                pass
        else:
            print("WHICH SYSTEM OF MEASUREMENT DO YOU PREFER?")
            print(" 1=METRIC     0=ENGLISH")
        while i > 1 or i < 0:
            try:
                m = input("ENTER THE APPROPRIATE NUMBER")
                i = int(m)
            except:
                pass
        return i


if __name__ == '__main__':
    try:
        r = Rockt2()
        r.instructions()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print(err)
