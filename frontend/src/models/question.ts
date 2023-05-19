
export class Question {
    public id: number = 0;
    public questionnaire: number = 0;
    public text: string = "";
    public created_at: Date = new Date();
    public question_type: string = "RD";
    public question_option_set: Array<number> = [];
}

