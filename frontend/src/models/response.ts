
import { Questionnaire } from "./questionnaire"
import { User } from "./user";

export class Response {
    public id: number = 0;
    public questionnaire: Questionnaire = new Questionnaire();
    public user: User = new User();
    public created_at: Date = new Date();
}