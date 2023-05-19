
import { Group } from "./group";

export class User {
    public id: number = 0;
    public first_name: string = "";
    public last_name: string = "";
    public username: string = "";
    public email: string = "";
    public groups: Array<Group> = [];
}