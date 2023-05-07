import { Component } from '@angular/core';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent {
  questions: number[] = [];
  title: string = 'Título do Meu Novo Formulário';

  handleNewQuestionClick() {
    console.log("title: " + this.title);
    console.log('New question clicked');
    this.questions.push(1);
    console.log(this.questions);
  }
}
