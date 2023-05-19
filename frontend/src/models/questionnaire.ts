
export class Questionnaire {
    public id: number = 0;
    public title: string = "";
    public description: string = "";
    public created_at: Date = new Date();
    public question_set: Array<number> = [];
}