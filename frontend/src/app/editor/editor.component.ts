import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { QuestionnariesService } from 'src/services/questionnaries.service';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css']
})
export class EditorComponent {
  questions: number[] = [];
  title: string = 'Título do Meu Novo Formulário';
  questionnarie: any;

  constructor(
    private route: ActivatedRoute,
    private questionnariesService: QuestionnariesService) {
  }

  ngOnInit() {
    // First get the product id from the current route.
    const routeParams = this.route.snapshot.paramMap;
    const questionnarieIdFromRoute: number = Number(routeParams.get('questionnarieId'));

    this.questionnariesService.getQuestionnarie(questionnarieIdFromRoute).subscribe((data: any) => {
      this.questionnarie = data;
    });
  }

  handleNewQuestionClick() {
    this.questions.push(1);
  }

  updateQuestionnarie() {
    this.questionnariesService.saveQuestionnarie(this.questionnarie).subscribe((data: any) => {
      this.questionnarie = data;
    });
  }
}
