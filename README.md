# week7-text-multimodal-ai
## Week 7: Text and Multimodal AI
- Text classifier: Clinical notes
- Image model: Chest X-Ray, Pneumonia vs Normal
- Pipeline: image model + text evidence -> JSON record
- Privacy: CNIC, phone, and email masked before logging
- ### Harmless or Harmful?
My system is only a triage / decision-support tool, not a final diagnosis.
It is harmless because it only shows evidence to the doctor.
It can be harmful if it is used alone as a doctor and a wrong Negative case is missed.
So low-confidence cases must always go for human review.
### Disagreement Case
Case: Text note says Pneumonia (0.8) but X-ray says Normal (0.9).
Fusion result is 0.45, confidence is only 0.55.
System should NOT give a final decision here.
It should send the case to "Needs Human Review" and show both evidences to the doctor.
