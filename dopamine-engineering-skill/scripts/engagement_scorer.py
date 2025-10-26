#!/usr/bin/env python3
"""
Engagement Scorer: Analyze apps/features for addiction risk

This script scores digital products based on dopamine engineering techniques
and flags potentially addictive patterns.

Usage:
    python engagement_scorer.py --interactive
    python engagement_scorer.py --analyze "feature_description.json"

Author: Claude Code
Version: 1.0
Date: 2025-10-23
"""

import json
import sys
from typing import Dict, List, Tuple
from dataclasses import dataclass, field
from enum import Enum


class RiskLevel(Enum):
    """Addiction risk classification"""
    LOW = "Low Risk"
    MODERATE = "Moderate Risk"
    HIGH = "High Risk"
    SEVERE = "Severe Risk - Do Not Build"


@dataclass
class Feature:
    """Represents a product feature to analyze"""
    name: str
    description: str
    techniques: List[str] = field(default_factory=list)
    scores: Dict[str, int] = field(default_factory=dict)
    total_score: int = 0
    risk_level: RiskLevel = RiskLevel.LOW
    warnings: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


# Scoring weights (0-10 scale)
TECHNIQUE_SCORES = {
    # Variable Rewards (High Risk)
    "variable_ratio_rewards": 9,
    "loot_boxes": 10,
    "random_rewards": 8,
    "mystery_mechanics": 7,

    # Infinite Engagement (High Risk)
    "infinite_scroll": 9,
    "autoplay": 8,
    "no_stopping_cues": 10,
    "endless_content": 9,

    # Social Pressure (Medium-High Risk)
    "streaks": 7,
    "fomo_mechanics": 8,
    "social_comparison": 6,
    "leaderboards": 5,
    "public_metrics": 6,

    # Notifications (Medium Risk)
    "push_notifications": 5,
    "high_frequency_notifications": 8,
    "fake_urgency_notifications": 9,
    "social_pressure_notifications": 7,

    # Time Pressure (Medium Risk)
    "countdown_timers": 6,
    "limited_time_events": 7,
    "expiring_content": 8,
    "timed_challenges": 5,

    # Investment Mechanics (Medium Risk)
    "sunk_cost_mechanics": 7,
    "collection_completion": 6,
    "progress_loss_threat": 9,
    "invested_time_tracking": 5,

    # Gamification (Low-Medium Risk)
    "points": 3,
    "badges": 4,
    "levels": 4,
    "achievements": 3,
    "progress_bars": 2,

    # Ethical Safeguards (Negative Scores - Good!)
    "usage_limits": -5,
    "take_a_break_reminders": -4,
    "stopping_cues": -6,
    "grayscale_mode": -3,
    "notification_batching": -4,
    "all_caught_up_message": -5,
    "wellbeing_metrics": -6,
    "easy_opt_out": -3,
}


def calculate_feature_score(feature: Feature) -> Feature:
    """Calculate addiction risk score for a feature"""

    total = 0
    for technique in feature.techniques:
        technique_lower = technique.lower().replace(" ", "_")
        if technique_lower in TECHNIQUE_SCORES:
            score = TECHNIQUE_SCORES[technique_lower]
            feature.scores[technique] = score
            total += score
        else:
            print(f"Warning: Unknown technique '{technique}'")

    feature.total_score = total

    # Determine risk level
    if total < 10:
        feature.risk_level = RiskLevel.LOW
    elif total < 25:
        feature.risk_level = RiskLevel.MODERATE
    elif total < 45:
        feature.risk_level = RiskLevel.HIGH
    else:
        feature.risk_level = RiskLevel.SEVERE

    # Generate warnings
    feature.warnings = generate_warnings(feature)

    # Generate recommendations
    feature.recommendations = generate_recommendations(feature)

    return feature


def generate_warnings(feature: Feature) -> List[str]:
    """Generate specific warnings based on detected techniques"""

    warnings = []

    # Check for gambling mechanics
    gambling_techniques = ["loot_boxes", "random_rewards", "variable_ratio_rewards"]
    if any(t.lower().replace(" ", "_") in gambling_techniques for t in feature.techniques):
        warnings.append("🚨 GAMBLING MECHANICS DETECTED - High addiction risk")
        warnings.append("   Legal implications in many jurisdictions")
        warnings.append("   Particularly harmful to vulnerable populations")

    # Check for infinite engagement
    infinite_techniques = ["infinite_scroll", "no_stopping_cues", "endless_content", "autoplay"]
    if any(t.lower().replace(" ", "_") in infinite_techniques for t in feature.techniques):
        warnings.append("⚠️  INFINITE ENGAGEMENT PATTERN - Users may lose time awareness")
        warnings.append("   Average session 3-5x longer than intended")

    # Check for FOMO mechanics
    fomo_techniques = ["fomo_mechanics", "expiring_content", "limited_time_events"]
    if any(t.lower().replace(" ", "_") in fomo_techniques for t in feature.techniques):
        warnings.append("⚠️  FOMO EXPLOITATION - Creates anxiety and compulsive checking")
        warnings.append("   Linked to decreased wellbeing in studies")

    # Check for lack of safeguards
    safeguards = ["usage_limits", "take_a_break_reminders", "stopping_cues"]
    if not any(t.lower().replace(" ", "_") in safeguards for t in feature.techniques):
        warnings.append("⚠️  NO SAFEGUARDS DETECTED - Add user protection features")

    # Check for notification overload
    notification_techniques = ["high_frequency_notifications", "fake_urgency_notifications"]
    if any(t.lower().replace(" ", "_") in notification_techniques for t in feature.techniques):
        warnings.append("⚠️  NOTIFICATION SPAM - Average >10 notifications/day")
        warnings.append("   High opt-out risk, negative brand perception")

    # Severe risk warning
    if feature.total_score >= 45:
        warnings.insert(0, "🛑 SEVERE ADDICTION RISK - STRONGLY RECOMMEND NOT BUILDING")
        warnings.insert(1, "   This design prioritizes engagement over user wellbeing")
        warnings.insert(2, "   Ethical and potential legal concerns")

    return warnings


def generate_recommendations(feature: Feature) -> List[str]:
    """Generate recommendations to reduce addiction risk"""

    recommendations = []

    # Always recommend safeguards
    safeguards = ["usage_limits", "take_a_break_reminders", "stopping_cues"]
    if not any(t.lower().replace(" ", "_") in safeguards for t in feature.techniques):
        recommendations.append("✅ ADD: Usage time limits and reminders")
        recommendations.append("✅ ADD: Natural stopping points ('You're all caught up!')")
        recommendations.append("✅ ADD: Screen time tracking dashboard")

    # If using infinite scroll
    if "infinite_scroll" in [t.lower().replace(" ", "_") for t in feature.techniques]:
        recommendations.append("✅ REPLACE: Infinite scroll with 'Load more' button")
        recommendations.append("✅ ADD: End-of-feed messages")

    # If using variable rewards
    variable_reward_techniques = ["variable_ratio_rewards", "loot_boxes", "random_rewards"]
    if any(t.lower().replace(" ", "_") in variable_reward_techniques for t in feature.techniques):
        recommendations.append("✅ REPLACE: Variable rewards with skill-based rewards")
        recommendations.append("✅ ADD: Transparent odds display")
        recommendations.append("✅ REMOVE: Pay-to-play random mechanics")

    # If using FOMO
    if "fomo_mechanics" in [t.lower().replace(" ", "_") for t in feature.techniques]:
        recommendations.append("✅ REFRAME: 'Limited time' to 'Coming back soon'")
        recommendations.append("✅ ADD: Grace periods and second chances")

    # If using streaks
    if "streaks" in [t.lower().replace(" ", "_") for t in feature.techniques]:
        recommendations.append("✅ ADD: Streak freeze/vacation mode")
        recommendations.append("✅ CHANGE: Weekly goals instead of daily pressure")

    # If using notifications
    notification_techniques = ["push_notifications", "high_frequency_notifications"]
    if any(t.lower().replace(" ", "_") in notification_techniques for t in feature.techniques):
        recommendations.append("✅ REDUCE: Max 3 notifications per day")
        recommendations.append("✅ ADD: Notification batching/summary mode")
        recommendations.append("✅ ADD: Granular notification controls")

    # If high risk
    if feature.risk_level in [RiskLevel.HIGH, RiskLevel.SEVERE]:
        recommendations.append("✅ CONDUCT: User wellbeing impact study")
        recommendations.append("✅ IMPLEMENT: Wellbeing metrics (not just engagement)")
        recommendations.append("✅ REVIEW: With ethics board before launch")

    # Always recommend transparency
    recommendations.append("✅ ENSURE: Transparent about techniques when asked")
    recommendations.append("✅ TEST: 'Would I want this used on my family?' test")

    return recommendations


def print_report(feature: Feature):
    """Print formatted analysis report"""

    print("\n" + "="*70)
    print(f"  ADDICTION RISK ANALYSIS: {feature.name}")
    print("="*70 + "\n")

    print(f"Description: {feature.description}\n")

    print("DETECTED TECHNIQUES:")
    print("-" * 70)
    for technique, score in sorted(feature.scores.items(), key=lambda x: x[1], reverse=True):
        indicator = "🔴" if score >= 8 else "🟡" if score >= 5 else "🟢" if score >= 0 else "💚"
        print(f"{indicator} {technique}: {score} points")
    print()

    print(f"TOTAL SCORE: {feature.total_score}")
    print(f"RISK LEVEL: {feature.risk_level.value}")
    print()

    if feature.warnings:
        print("WARNINGS:")
        print("-" * 70)
        for warning in feature.warnings:
            print(warning)
        print()

    if feature.recommendations:
        print("RECOMMENDATIONS:")
        print("-" * 70)
        for rec in feature.recommendations:
            print(rec)
        print()

    print("="*70)
    print()


def interactive_mode():
    """Interactive CLI for analyzing features"""

    print("\n" + "="*70)
    print("  ENGAGEMENT SCORER - Interactive Mode")
    print("="*70 + "\n")

    print("This tool analyzes features for addiction risk based on dopamine")
    print("engineering techniques. Be honest for accurate assessment.\n")

    name = input("Feature name: ")
    description = input("Brief description: ")

    print("\nSelect all techniques used (comma-separated, or 'list' to see options):\n")

    user_input = input("> ")

    if user_input.lower() == 'list':
        print("\nAvailable techniques:")
        for i, technique in enumerate(sorted(TECHNIQUE_SCORES.keys()), 1):
            score = TECHNIQUE_SCORES[technique]
            risk = "HIGH" if score >= 8 else "MEDIUM" if score >= 5 else "LOW" if score >= 0 else "SAFEGUARD"
            print(f"{i}. {technique.replace('_', ' ').title()} ({risk})")
        print()
        user_input = input("Enter technique names (comma-separated): ")

    techniques = [t.strip() for t in user_input.split(",")]

    feature = Feature(name=name, description=description, techniques=techniques)
    feature = calculate_feature_score(feature)

    print_report(feature)

    # Ask if user wants to export
    export = input("Export to JSON? (y/n): ")
    if export.lower() == 'y':
        filename = input("Filename (default: feature_analysis.json): ") or "feature_analysis.json"
        export_to_json(feature, filename)
        print(f"✅ Exported to {filename}")


def export_to_json(feature: Feature, filename: str):
    """Export analysis to JSON file"""

    data = {
        "name": feature.name,
        "description": feature.description,
        "techniques": feature.techniques,
        "scores": feature.scores,
        "total_score": feature.total_score,
        "risk_level": feature.risk_level.value,
        "warnings": feature.warnings,
        "recommendations": feature.recommendations
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


def analyze_from_file(filename: str):
    """Analyze feature from JSON file"""

    with open(filename, 'r') as f:
        data = json.load(f)

    feature = Feature(
        name=data.get("name", "Unknown"),
        description=data.get("description", ""),
        techniques=data.get("techniques", [])
    )

    feature = calculate_feature_score(feature)
    print_report(feature)

    return feature


def quick_examples():
    """Show example analyses for common patterns"""

    examples = [
        Feature(
            name="Social Media Feed",
            description="Infinite scrolling feed with variable content quality",
            techniques=[
                "infinite_scroll",
                "variable_ratio_rewards",
                "autoplay",
                "no_stopping_cues",
                "push_notifications",
                "social_comparison"
            ]
        ),
        Feature(
            name="Duolingo-Style Learning",
            description="Gamified language learning with streaks",
            techniques=[
                "streaks",
                "points",
                "levels",
                "achievements",
                "push_notifications",
                "usage_limits",
                "stopping_cues"
            ]
        ),
        Feature(
            name="Gacha Game",
            description="Character collection with randomized loot boxes",
            techniques=[
                "loot_boxes",
                "variable_ratio_rewards",
                "collection_completion",
                "limited_time_events",
                "fomo_mechanics",
                "sunk_cost_mechanics",
                "progress_loss_threat"
            ]
        )
    ]

    print("\n" + "="*70)
    print("  EXAMPLE ANALYSES")
    print("="*70 + "\n")

    for example in examples:
        feature = calculate_feature_score(example)
        print_report(feature)
        input("Press Enter for next example...")


def main():
    """Main CLI entry point"""

    if len(sys.argv) == 1:
        print("Usage:")
        print("  python engagement_scorer.py --interactive")
        print("  python engagement_scorer.py --analyze <file.json>")
        print("  python engagement_scorer.py --examples")
        sys.exit(1)

    command = sys.argv[1]

    if command == "--interactive":
        interactive_mode()
    elif command == "--analyze" and len(sys.argv) > 2:
        analyze_from_file(sys.argv[2])
    elif command == "--examples":
        quick_examples()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
