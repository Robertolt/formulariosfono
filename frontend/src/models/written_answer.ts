
import { Question } from "./question";
import { Response } from "./response";

export class WrittenAnswer {
    public id: number = 0;
    public response: Response = new Response();
    public question: Question = new Question();
    public text: string = "";
    public updated_at: Date = new Date();
}
