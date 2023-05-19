import { QuestionOption } from "./question_option";

export class SelectedOption {
    public id: number = 0;
    public response: Response = new Response();
    public question_option: QuestionOption = new QuestionOption();
    public updated_at: Date = new Date();
}