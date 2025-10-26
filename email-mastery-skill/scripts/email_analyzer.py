#!/usr/bin/env python3
"""
Email Quality Analyzer
Analyzes email content and provides quality score with recommendations
"""

import re
from typing import Dict, List, Tuple


class EmailAnalyzer:
    """Analyzes email content for quality and deliverability"""

    # Spam trigger words (use sparingly)
    SPAM_WORDS = [
        'free', '100%', 'guarantee', 'no cost', 'prize', 'winner', 'cash',
        'earn money', 'extra income', 'work from home', 'click here',
        'act now', 'limited time', 'urgent', 'winner', 'congratulations',
        'you have been selected', 'claim now', 'order now', 'exclusive deal'
    ]

    # Power words (good to use)
    POWER_WORDS = [
        'you', 'new', 'proven', 'results', 'easy', 'quick', 'simple',
        'discover', 'secret', 'unlock', 'transform', 'amazing', 'exclusive',
        'limited', 'instant', 'guaranteed', 'powerful'
    ]

    def __init__(self):
        self.score = 100
        self.issues = []
        self.recommendations = []
        self.highlights = []

    def analyze_subject_line(self, subject: str) -> Dict:
        """Analyze subject line quality"""
        results = {
            'score': 100,
            'length_ok': False,
            'personalization': False,
            'spam_triggers': [],
            'power_words': [],
            'emoji_count': 0,
            'punctuation_issues': False
        }

        # Length check (40-60 chars ideal)
        length = len(subject)
        if 40 <= length <= 60:
            results['length_ok'] = True
        elif length < 30:
            results['score'] -= 10
            self.issues.append(f"Subject line too short ({length} chars). Aim for 40-60.")
        elif length > 70:
            results['score'] -= 15
            self.issues.append(f"Subject line too long ({length} chars). Gets cut off on mobile.")

        # Personalization check
        if '{name}' in subject.lower() or '{{' in subject:
            results['personalization'] = True
            results['score'] += 10
            self.highlights.append("Good: Uses personalization token")

        # Spam trigger words
        subject_lower = subject.lower()
        for word in self.SPAM_WORDS:
            if word in subject_lower:
                results['spam_triggers'].append(word)
                results['score'] -= 5

        if results['spam_triggers']:
            self.issues.append(f"Contains spam triggers: {', '.join(results['spam_triggers'])}")

        # Power words
        for word in self.POWER_WORDS:
            if word in subject_lower:
                results['power_words'].append(word)

        # Emoji check
        emoji_count = sum(1 for c in subject if ord(c) > 127)
        results['emoji_count'] = emoji_count
        if emoji_count > 2:
            results['score'] -= 10
            self.issues.append(f"Too many emojis ({emoji_count}). Max 1-2 recommended.")

        # Punctuation issues
        if subject.count('!') > 1:
            results['punctuation_issues'] = True
            results['score'] -= 10
            self.issues.append("Too many exclamation marks. Max 1 recommended.")

        if subject.isupper():
            results['punctuation_issues'] = True
            results['score'] -= 20
            self.issues.append("ALL CAPS subject line. Major spam trigger.")

        return results

    def analyze_preview_text(self, preview: str) -> Dict:
        """Analyze preview text"""
        results = {
            'score': 100,
            'length_ok': False,
            'complements_subject': True
        }

        # Length check (40-90 chars ideal)
        length = len(preview)
        if 40 <= length <= 90:
            results['length_ok'] = True
            self.highlights.append("Preview text length is optimal")
        elif length < 20:
            results['score'] -= 15
            self.issues.append("Preview text too short. Aim for 40-90 characters.")
        elif length > 120:
            results['score'] -= 10
            self.issues.append("Preview text too long. Gets cut off.")

        return results

    def analyze_email_body(self, body: str) -> Dict:
        """Analyze email body content"""
        results = {
            'score': 100,
            'word_count': 0,
            'link_count': 0,
            'image_mentions': 0,
            'has_cta': False,
            'has_ps': False,
            'spam_score': 0
        }

        # Word count
        words = body.split()
        results['word_count'] = len(words)

        if len(words) < 50:
            results['score'] -= 5
            self.issues.append("Email quite short. May lack substance.")
        elif len(words) > 800:
            results['score'] -= 10
            self.issues.append("Email very long. Consider shortening.")

        # Link count
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
        results['link_count'] = len(links)

        if len(links) > 10:
            results['score'] -= 15
            self.issues.append(f"Too many links ({len(links)}). Spam trigger. Keep to 3-5.")

        # URL shorteners (spam trigger)
        if any(short in body.lower() for short in ['bit.ly', 'tinyurl', 'goo.gl', 't.co']):
            results['score'] -= 20
            self.issues.append("Contains URL shorteners. Major spam trigger.")

        # CTA check
        cta_patterns = [
            r'\[.*?\]',  # [Button text]
            r'click here',
            r'get started',
            r'download',
            r'sign up',
            r'join now',
            r'buy now',
            r'learn more'
        ]
        for pattern in cta_patterns:
            if re.search(pattern, body.lower()):
                results['has_cta'] = True
                self.highlights.append("Has clear call-to-action")
                break

        if not results['has_cta']:
            results['score'] -= 15
            self.issues.append("No clear call-to-action found")

        # P.S. check
        if re.search(r'p\.?s\.?', body.lower()):
            results['has_ps'] = True
            self.highlights.append("Has P.S. (90% of people read this)")

        # Spam word density
        body_lower = body.lower()
        spam_count = sum(1 for word in self.SPAM_WORDS if word in body_lower)
        spam_density = (spam_count / len(words)) * 100 if words else 0
        results['spam_score'] = spam_density

        if spam_density > 2:
            results['score'] -= 20
            self.issues.append(f"High spam word density ({spam_density:.1f}%)")

        # Personalization
        if '{name}' in body.lower() or '{{' in body:
            self.highlights.append("Uses personalization in body")
            results['score'] += 5

        return results

    def check_structure(self, body: str) -> Dict:
        """Check email structure"""
        results = {
            'score': 100,
            'has_hook': False,
            'has_value': True,
            'paragraphs': 0
        }

        # Paragraph count (too many = hard to read)
        paragraphs = [p for p in body.split('\n\n') if p.strip()]
        results['paragraphs'] = len(paragraphs)

        if len(paragraphs) > 15:
            results['score'] -= 10
            self.issues.append("Many paragraphs. Consider breaking into sections.")

        # Hook check (first 2 sentences should grab attention)
        first_sentences = '. '.join(body.split('.')[:2])
        hook_indicators = ['you', 'ever', 'imagine', 'what if', 'question', 'discovered']
        if any(indicator in first_sentences.lower() for indicator in hook_indicators):
            results['has_hook'] = True
            self.highlights.append("Strong opening hook")

        return results

    def analyze_full_email(self, subject: str, preview: str, body: str) -> Dict:
        """Analyze complete email"""
        self.score = 100
        self.issues = []
        self.recommendations = []
        self.highlights = []

        # Analyze components
        subject_results = self.analyze_subject_line(subject)
        preview_results = self.analyze_preview_text(preview)
        body_results = self.analyze_email_body(body)
        structure_results = self.check_structure(body)

        # Calculate weighted score
        total_score = (
            subject_results['score'] * 0.4 +  # Subject is 40% of decision
            preview_results['score'] * 0.2 +   # Preview is 20%
            body_results['score'] * 0.3 +      # Body is 30%
            structure_results['score'] * 0.1   # Structure is 10%
        )

        # Generate recommendations
        self._generate_recommendations(
            subject_results, preview_results, body_results, structure_results
        )

        # Determine grade
        grade = self._calculate_grade(total_score)

        # Expected performance
        expected_opens, expected_clicks = self._estimate_performance(total_score)

        return {
            'overall_score': round(total_score, 1),
            'grade': grade,
            'expected_open_rate': expected_opens,
            'expected_click_rate': expected_clicks,
            'issues': self.issues,
            'highlights': self.highlights,
            'recommendations': self.recommendations,
            'components': {
                'subject': subject_results,
                'preview': preview_results,
                'body': body_results,
                'structure': structure_results
            }
        }

    def _generate_recommendations(self, subject_r, preview_r, body_r, structure_r):
        """Generate actionable recommendations"""

        # Subject line recommendations
        if not subject_r['length_ok']:
            self.recommendations.append(
                "Optimize subject line to 40-60 characters for best mobile display"
            )

        if not subject_r['personalization']:
            self.recommendations.append(
                "Add personalization token ({Name}) to subject line for 15-25% lift"
            )

        if len(subject_r['power_words']) < 2:
            self.recommendations.append(
                "Include 1-2 power words in subject (you, new, proven, quick, secret)"
            )

        # Preview text
        if not preview_r['length_ok']:
            self.recommendations.append(
                "Optimize preview text to 40-90 characters"
            )

        # Body recommendations
        if not body_r['has_cta']:
            self.recommendations.append(
                "Add clear call-to-action (button or link with action-oriented text)"
            )

        if not body_r['has_ps']:
            self.recommendations.append(
                "Add P.S. at end (90% of people read it - use for urgency/social proof)"
            )

        if body_r['link_count'] == 0:
            self.recommendations.append(
                "Add at least one link/CTA to drive action"
            )

        # Structure recommendations
        if not structure_r['has_hook']:
            self.recommendations.append(
                "Strengthen opening hook - first 2 sentences should grab attention"
            )

        # General recommendations
        if body_r['spam_score'] > 1:
            self.recommendations.append(
                "Reduce spam trigger words for better deliverability"
            )

    def _calculate_grade(self, score: float) -> str:
        """Calculate letter grade"""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    def _estimate_performance(self, score: float) -> Tuple[str, str]:
        """Estimate expected open and click rates"""
        if score >= 90:
            return "40-55%", "12-18%"
        elif score >= 80:
            return "30-45%", "8-14%"
        elif score >= 70:
            return "25-35%", "5-10%"
        elif score >= 60:
            return "18-28%", "3-7%"
        else:
            return "10-20%", "1-4%"


def print_analysis(results: Dict):
    """Pretty print analysis results"""
    print("\n" + "="*60)
    print("EMAIL QUALITY ANALYSIS")
    print("="*60)

    print(f"\nOVERALL SCORE: {results['overall_score']}/100 (Grade: {results['grade']})")
    print(f"\nEXPECTED PERFORMANCE:")
    print(f"  Open Rate: {results['expected_open_rate']}")
    print(f"  Click Rate: {results['expected_click_rate']}")

    if results['highlights']:
        print(f"\n✅ STRENGTHS:")
        for highlight in results['highlights']:
            print(f"  • {highlight}")

    if results['issues']:
        print(f"\n⚠️  ISSUES:")
        for issue in results['issues']:
            print(f"  • {issue}")

    if results['recommendations']:
        print(f"\n💡 RECOMMENDATIONS:")
        for i, rec in enumerate(results['recommendations'], 1):
            print(f"  {i}. {rec}")

    print("\n" + "="*60 + "\n")


def main():
    """Example usage"""

    # Example email
    subject = "Sarah, quick question about your email list"
    preview = "I'm curious about something..."
    body = """Hey Sarah,

Quick question:

When you think about growing your email list, what's the
#1 thing that frustrates you most?

Is it:
A) Getting traffic to your opt-in page
B) Creating lead magnets people actually want
C) Converting visitors into subscribers
D) Something else entirely

Hit reply and let me know - I'm genuinely curious.

(And if you tell me, I'll send you a free resource
that specifically addresses your challenge.)

Talk soon,
James

P.S. I read every reply. Seriously."""

    # Analyze
    analyzer = EmailAnalyzer()
    results = analyzer.analyze_full_email(subject, preview, body)

    # Print results
    print_analysis(results)

    # Example of low-quality email for comparison
    print("\n\n" + "="*60)
    print("COMPARING TO LOW-QUALITY EMAIL:")
    print("="*60)

    bad_subject = "FREE!!! URGENT: Click here NOW to win $1000!!!"
    bad_preview = "Limited time offer"
    bad_body = """CONGRATULATIONS!!!

You have been selected to receive a FREE prize worth $1000!

Click here: http://bit.ly/scam
Click here: http://tinyurl.com/fake
Click here: http://goo.gl/spam

ACT NOW! This offer expires in 24 hours!

FREE FREE FREE!!!

Buy now! Order now! Click here!"""

    bad_results = analyzer.analyze_full_email(bad_subject, bad_preview, bad_body)
    print_analysis(bad_results)


if __name__ == "__main__":
    main()
