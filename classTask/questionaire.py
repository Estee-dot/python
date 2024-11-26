import java.util.Scanner;

public class Questionaire{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	String[][] questions = {
	{"A. expend energy, enjoy group", \t\t"B. conserve energy, enjoy one on one"};
	{"A. Interpret literally", \t\t"B. look for meaning and possibilities"};
	{"A. Logical, thinking, questioning", \t\t"B. Empathetic, feeling, accomadating"};
	{"A. organized, orderly", \t\t"B. Flexible, adaptable"};
	{"A. more outgoing, think out loud \t\tB. more reserved, think to yourself"};
	{"A. Practical, realistic, experiential", \t\t"B. Imaginative, innovative, theoretical"};
	{"A. Candid, straight forward, frank", \t\t"B. Tactful, kind, encouraging"};
	{"A. Plan, schedule", \t\t"B. unplanned, Spontaneous"};
	{"A. Seek many tasks, public activities, interaction with others", \t\t"B. seek private, solitary activites with quiet to concentrate"};
	{"A. Standard, usual, conventional", \t\t"B. Different, novel, uniques"};
	{"firm, tend to criticize, hold the line", \t\t"B. gentle, tend to appreciate, conciliate"};
	{"regulated, structured", \t\t"B. Easy-going, live and let live"};
	{"A.External, communicative, express yourself", \t\t"B. Internal, reticent, keep to yourself"};
	{"A. Focus on here-and-now", \t\t"B. Look to the future, global prespective, big picture"};
	{"A. tough-minded, just", \t\t"B. tender-hearted, merciful"};
	{"A. preparation, plan ahead", \t\t"B. go with the flow, adapt as you go"};
	{"A. Active, initiate", \t\t"B. reflective, deliberate"};
	{"A. facts, things, what is", \t\t"B. ideas, dreams , what could be, philosophical"};
	{"A. matter of fact, issue-oriented", \t\t"B. sensitive, people-oriented, compassionate"};
	{"A. control, govern", \t\t"B. latitude, freedom"};

	}

	String[] answers = new String[20];
	System.out.print("What is your name?");
	String response = input.next();

	for(int question = 0; question <= questions.length; question++){
		System.out.print(questions[question][0]);
		System.out.print(questions[question][1]);

		System.out.print("Select option A or B");
		char options = input.next().charAt(0);

			if(options == 'A'){
				answers[].add(questions[question][0]);
			}
			else if(options == 'B'){
				answers[].add(questions[question][1]);
			}
			else{
				System.out.print("Enter A or B: ");
			}
	
	}









}


}