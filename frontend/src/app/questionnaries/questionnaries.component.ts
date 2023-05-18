import { Component } from '@angular/core';
import { QuestionnariesService } from 'src/services/questionnaries.service';

@Component({
  selector: 'app-questionnaries',
  templateUrl: './questionnaries.component.html',
  styleUrls: ['./questionnaries.component.css']
})
export class QuestionnariesComponent {
  questionnaries!: any;

  constructor(private questionnariesService: QuestionnariesService) {
  }

  ngOnInit() {
    this.questionnariesService.getQuestionnaries().subscribe((data: any) => {
      this.questionnaries = data;
    });
  }
}
