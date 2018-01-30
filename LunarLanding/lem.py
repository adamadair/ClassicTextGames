import sys
import math


class PlayerWin(Exception):
    """Thrown when a player lands the lunar module."""


class PlayerLose(Exception):
    """Thrown when a player loses for any reason."""


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

    def __print_instructions(self, q):
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
        self.__set_measurement_option(q)
        self.__print_instructions(q)
        try:
            while True:
                # this is the game loop
                self.__update_lunar_module_spatial_position()
                self.__update_and_print_output()
                self.__check_craft_status()
                self.__get_tpa_from_user()

        except PlayerLose as end:
            print(end)
        except PlayerWin as end:
            print(end)
        except Exception as error:
            print(error)
        # for i in range(self.n - 1):
        #    if self.M1 != 0:

    def __set_measurement_option(self, q):
        """
        Allow the user to choose between metric or english measurements.
        :param q: expecting 'yes' or 'no'
        """
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
        self.K = i
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

    def __get_tpa_from_user(self):
        if self.M1 <= 0:
            # no fuel so just return defaults
            self.T1 = 20
            self.F = 0.0
            self.P = 0.0
            return
        print()
        tpa = None
        while tpa is None:
            tpa = input("T,P,A? ").split(',')
            if len(tpa) != 3:
                tpa = None
                continue
            try:
                self.T1 = int(tpa[0])
                self.F = float(tpa[1])
                self.p = float(tpa[2])
                self.F /= 100
                if self.T1 < 0:
                    print("\nTHIS SPACECRAFT IS NOT ABLE TO VIOLATE THE SPACE-TIME CONTINUUM.")
                    tpa = None
                    continue
                if self.T1 == 0:
                    raise PlayerLose("MISSION ABENDED")
                abf = abs(self.F - 0.05)
                if abf > 1 or abf < 0.05:
                    print("IMPOSSIBLE THRUST VALUE {0}".format(self.__failed_thrust_reason(self.F)))
                    tpa = None
                    continue
                if abs(self.P) > 180:
                    print("\nIF YOU WANT TO SPIN AROUND, GO OUTSIDE THE MODULE\nFOR AN E.V.A.")
                    tpa = None
                    continue

            except:
                tpa = None

    def __failed_thrust_reason(self, f):
        if f < 0:
            return "NEGATIVE"
        if f - 0.05 < 0.05:
            return "TOO SMALL"
        return "TOO LARGE"

    def __update_lunar_module_trajectory(self):
        self.N = 20
        if self.T1 >= 400:
            self.N = self.T1 / 20
        self.T1 /= self.N
        self.P = self.P * 3.14159 / 180
        self.S = math.sin(self.P)
        self.C = math.cos(self.P)
        self.M2 = self.M0 * self.T1 * self.F / self.B
        self.R3 = -.5 * self.R0 * ((self.V0 / self.R) ** 2) + self.R * self.A1 * self.A1
        self.A3 = - 2 * self.R1 * self.A1 / self.R

    def __update_lunar_module_spatial_position(self):
        for i in range(1, self.N + 1):
            if self.M1 > 0:
                # update the fuel situation
                self.M1 = self.M1 - self.M2
                if self.M1 <= 0:
                    # ran out of fuel
                    self.F = self.F * (1 + self.M1 / self.M2)
                    self.M2 = self.M1 + self.M2
                    print("YOU ARE OUT OF FUEL.")
                    self.M1 = 0
            else:
                # out of fuel
                self.F = 0
                self.M2 = 0
            self.M = self.M - .5 * self.M2

            self.R4 = self.R3
            self.R3 = -.5 * self.R0 * ((self.V0 / self.R) ** 2) + self.R * self.A1 * self.A1
            self.R2 = (3 * self.R3 - self.R4) / 2 + 0.00526 * self.F1 * self.F * self.C / self.M
            self.A4 = self.A3
            self.A3 = -2 * self.R1 * self.A1 / self.R
            self.A2 = (3 * self.A3 - self.A4) / 2 + 0.0056 * self.F1 * self.F * self.S / (self.M * self.R)
            self.X = self.R1 * self.T1 + 0.5 * self.R2 * self.T1 * self.T1
            self.R = self.R + self.X
            self.H0 = self.H0 + self.X
            self.R1 = self.R1 + self.R2 * self.T1
            self.A = self.A + self.A1 * self.T1 + 0.5 * self.A2 * self.T1 * self.T1
            self.A1 = self.A1 + self.A2 * self.T1
            self.M = self.M - 0.5 * self.M2
            self.T = self.T + self.T1
            if self.H0 < 3.287828E-04:
                return

    def __update_and_print_output(self):
        self.H = self.H0 * self.Z
        self.H1 = self.R1 * self.Z
        self.D = self.R0 * self.A * self.Z
        self.D1 = self.R * self.A1 * self.Z
        self.T2 = self.M1 * self.B / self.M0
        print(" {0:9}{1:12} {2:13} {3:11} {4:10} {5}".format(str(self.T), str(self.H), str(self.D), str(self.H1),
                                                             str(self.D1), str(self.T2)))

    def __check_craft_status(self):
        if self.H0 < 3.287828E-04:
            if self.R1 < - 8.21957E-04:
                self.__crash()
            if abs(self.R * self.A1) > 4.93174E-04:
                self.__crash()
            if self.H0 < -3.287828E-04:
                self.__crash()
            if abs(self.D) > 10 * self.Z:
                self.__landed()
            self.__won()
        if self.R0 * self.A > 164.474:
            self.__lost_in_space()

    def __crash(self):
        msg = "CRASH !!!!!!!!!!!!!!!!"
        msg += "\nYOUR IMPACT CREATED A CRATER {0} {1} DEEP.".format(abs(self.H), self.M_STR)
        x1 = math.sqrt(self.D1 * self.D1 + self.H1 * self.H1) * self.G3
        msg += "AT CONTACT YOU WERE TRAVELING {0} {1}/HR".format(x1, self.N_STR)
        raise PlayerLose(msg)

    def __lost_in_space(self):
        raise PlayerLose("\nYOU HAVE BEEN LOST IN SPACE WITH NO HOPE OF RECOVERY.")

    def __landed(self):
        msg = "YOU ARE DOWN SAFELY - \n\n"
        msg += "BUT MISSED THE LANDING SITE BY {0} {1}.".format(abs(self.D / self.G5), self.N_STR)
        raise PlayerLose(msg)

    def __won(self):
        msg = "TRANQUILITY BASE HERE -- THE EAGLE HAS LANDED.\nCONGRATULATIONS -- THERE WAS NO SPACECRAFT DAMAGE."
        msg += "\nYOU MAY NOW PROCEED WITH SURFACE EXPLORATION."
        raise PlayerWin(msg)


if __name__ == '__main__':
    try:
        if sys.version_info < (3,):
            raise Exception("LEM requires Python 3.0 or higher.")
        run_me = True
        while run_me:
            r = Rockt2()
            r.run()
            resp = r.user_choice("DO YOU WANT TO TRY IT AGAIN (YES/NO)? ", ['yes', 'no'])
            run_me = resp == 'yes'
        print("\nTOO BAD, THE SPACE PROGRAM HATES TO LOSE EXPERIENCED\nASTRONAUTS.")
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print(err)
