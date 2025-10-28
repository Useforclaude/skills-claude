---
name: algorithmic-trading-skill
description: Master algorithmic trading strategy design and systematic trading. Use for strategy development (trend following, mean reversion, breakout, arbitrage, momentum strategies), backtesting frameworks (Backtrader, QuantConnect, Zipline), parameter optimization (grid search, genetic algorithms, walk-forward analysis), performance metrics (Sharpe ratio, Sortino, Calmar, max drawdown, profit factor), live trading deployment, risk management integration, data quality handling, execution algorithms (TWAP, VWAP), and building production-ready algorithmic trading systems for Forex, Crypto, and Stocks. Also use for Thai keywords "เทรดอัตโนมัติ", "บอทเทรด", "สร้างบอทเทรด", "ระบบเทรด", "กลยุทธ์เทรด", "backtesting", "ทดสอบย้อนหลัง", "เทรดอัลกอริทึม", "โปรแกรมเทรด", "เทรดคริปโต", "เทรดหุ้น", "เทรดฟอเร็กซ์", "ปั้นกำไรอัตโนมัติ", "จัดการความเสี่ยง", "Sharpe ratio", "วัดผลเทรด", "เทรดระบบ".. Also use for Thai keywords "เทรด", "ซื้อขาย", "การเทรด", "อัตโนมัติ", "ทำให้อัตโนมัติ", "ลดขั้นตอน", "วิเคราะห์กราฟ", "วิเคราะห์เทคนิค", "กราฟหุ้น"
---

# 🤖 Algorithmic Trading Mastery Skill

> **Master systematic trading strategy design, backtesting, and deployment**
>
> **Strategies:** Trend | Mean Reversion | Breakout | Arbitrage | Statistical
>
> **Frameworks:** Backtrader | QuantConnect | Zipline | Custom

---

## 📚 Table of Contents

1. [Algorithmic Trading Fundamentals](#fundamentals)
2. [Strategy Types & Design](#strategy-types)
3. [Backtesting Frameworks](#backtesting)
4. [Parameter Optimization](#optimization)
5. [Performance Metrics](#performance-metrics)
6. [Walk-Forward Analysis](#walk-forward)
7. [Live Trading Deployment](#live-trading)
8. [Risk Management Integration](#risk-management)
9. [Execution Algorithms](#execution)
10. [Production Best Practices](#production)

---

## 1. Algorithmic Trading Fundamentals {#fundamentals}

### 🎯 Why Algorithmic Trading?

**Advantages:**
```
✅ Removes emotion from trading
✅ Backtestable (know edge before risking capital)
✅ Consistent execution (no discretion)
✅ 24/7 operation (crypto markets)
✅ Fast execution (milliseconds)
✅ Handles multiple markets simultaneously
✅ Scalable (add capital without degradation)
```

**Challenges:**
```
⚠️ Requires programming skills
⚠️ Data quality critical
⚠️ Overfitting risk (curve fitting)
⚠️ Market regime changes
⚠️ Execution slippage
⚠️ Technical failures
⚠️ Requires continuous monitoring
```

---

## 2. Strategy Types & Design {#strategy-types}

### 🎯 Major Strategy Categories

**1. Trend Following** ⭐⭐⭐⭐⭐
```
Philosophy: "The trend is your friend"

Entry Rules:
- Price > Moving Average
- MACD crossover
- ADX > 25 (strong trend)
- Higher highs + higher lows

Exit Rules:
- Opposite signal
- Trailing stop
- Trend strength weakens

Pros:
✅ Large winners (ride trends)
✅ Simple to code
✅ Works across all markets

Cons:
❌ Low win rate (~40%)
❌ Whipsaws in ranging markets
❌ Requires patience

Best Markets: Forex majors, Crypto, Stock indices
Best Timeframes: H4, Daily
```

**Python Example:**
```python
import backtrader as bt

class MovingAverageCrossover(bt.Strategy):
    params = (
        ('fast_period', 10),
        ('slow_period', 30),
    )

    def __init__(self):
        self.fast_ma = bt.indicators.SMA(self.data.close, period=self.p.fast_period)
        self.slow_ma = bt.indicators.SMA(self.data.close, period=self.p.slow_period)
        self.crossover = bt.indicators.CrossOver(self.fast_ma, self.slow_ma)

    def next(self):
        if not self.position:
            if self.crossover > 0:  # Fast crosses above slow
                self.buy()
        else:
            if self.crossover < 0:  # Fast crosses below slow
                self.close()
```

---

**2. Mean Reversion** ⭐⭐⭐⭐
```
Philosophy: "What goes up must come down (and vice versa)"

Entry Rules:
- Price deviates X standard deviations from mean
- RSI < 30 (oversold) or > 70 (overbought)
- Bollinger Band touches
- Z-score thresholds

Exit Rules:
- Price returns to mean
- Opposite extreme
- Time-based exit

Pros:
✅ High win rate (~60-70%)
✅ Frequent trades
✅ Good for ranging markets

Cons:
❌ Small winners
❌ Catastrophic losses in trends
❌ Requires tight risk management

Best Markets: Stock pairs, FX pairs, Options
Best Timeframes: M15, H1, H4
```

**Python Example:**
```python
class BollingerMeanReversion(bt.Strategy):
    params = (
        ('period', 20),
        ('devfactor', 2),
    )

    def __init__(self):
        self.boll = bt.indicators.BollingerBands(
            self.data.close,
            period=self.p.period,
            devfactor=self.p.devfactor
        )

    def next(self):
        if not self.position:
            # Buy at lower band
            if self.data.close[0] < self.boll.lines.bot[0]:
                self.buy()
        else:
            # Exit at middle band or upper band
            if self.data.close[0] > self.boll.lines.mid[0]:
                self.close()
```

---

**3. Breakout Trading** ⭐⭐⭐⭐
```
Philosophy: "Follow momentum after consolidation"

Entry Rules:
- Price breaks above resistance
- Volume confirmation (Volume > avg × 1.5)
- Multiple timeframe alignment
- Volatility contraction → expansion

Exit Rules:
- Fixed target (ATR-based)
- Trailing stop
- Support/resistance flip

Pros:
✅ Catches major moves
✅ Clear entry signals
✅ Works in trending markets

Cons:
❌ Many false breakouts
❌ Requires patience
❌ Slippage on volatile breakouts

Best Markets: Stocks, Crypto
Best Timeframes: Daily, H4
```

---

**4. Statistical Arbitrage (Pairs Trading)** ⭐⭐⭐⭐⭐
```
Philosophy: "Exploit temporary divergences between correlated assets"

Process:
1. Find correlated pairs (correlation > 0.8)
2. Calculate spread (price A - hedge_ratio × price B)
3. Z-score = (spread - mean) / std_dev
4. Enter: |Z-score| > 2
5. Exit: Z-score → 0

Pros:
✅ Market neutral (hedge)
✅ Statistical edge
✅ Lower volatility

Cons:
❌ Correlations break down
❌ Requires execution precision
❌ Capital intensive (need both legs)

Best Markets: Stock pairs, FX pairs, Crypto pairs
```

**Python Example:**
```python
import numpy as np
import pandas as pd

class PairsTradingStrategy:
    def __init__(self, asset1, asset2, lookback=60, entry_z=2, exit_z=0.5):
        self.asset1 = asset1
        self.asset2 = asset2
        self.lookback = lookback
        self.entry_z = entry_z
        self.exit_z = exit_z

    def calculate_hedge_ratio(self, prices1, prices2):
        """Calculate optimal hedge ratio using linear regression"""
        return np.polyfit(prices2, prices1, 1)[0]

    def calculate_spread(self, prices1, prices2, hedge_ratio):
        """Calculate spread between pairs"""
        return prices1 - hedge_ratio * prices2

    def calculate_zscore(self, spread):
        """Calculate Z-score of spread"""
        mean = spread.rolling(self.lookback).mean()
        std = spread.rolling(self.lookback).std()
        return (spread - mean) / std

    def generate_signals(self, prices1, prices2):
        """Generate trading signals"""
        hedge_ratio = self.calculate_hedge_ratio(prices1[-self.lookback:], prices2[-self.lookback:])
        spread = self.calculate_spread(prices1, prices2, hedge_ratio)
        zscore = self.calculate_zscore(spread)

        signals = pd.DataFrame(index=prices1.index)
        signals['hedge_ratio'] = hedge_ratio
        signals['spread'] = spread
        signals['zscore'] = zscore

        # Entry signals
        signals['long_entry'] = zscore < -self.entry_z   # Long asset1, short asset2
        signals['short_entry'] = zscore > self.entry_z   # Short asset1, long asset2

        # Exit signals
        signals['exit'] = abs(zscore) < self.exit_z

        return signals
```

---

## 3. Backtesting Frameworks {#backtesting}

### 🎯 Framework Comparison

| Feature | Backtrader | QuantConnect | Zipline | Custom |
|---------|------------|--------------|---------|--------|
| **Language** | Python | Python/C# | Python | Any |
| **Ease of Use** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| **Speed** | Medium | Fast | Medium | Very Fast |
| **Data Sources** | CSV, API | Built-in (stocks/crypto) | CSV, Bundle | Custom |
| **Live Trading** | Yes | Yes (cloud) | Limited | Yes |
| **Cost** | Free | Free tier | Free | Free |
| **Best For** | Forex/Crypto | US Stocks | Quantitative | Specialized |

---

### 🎯 Complete Backtest Setup (Backtrader)

```python
import backtrader as bt
import pandas as pd
from datetime import datetime

# ==================== STRATEGY ====================
class TrendFollowingStrategy(bt.Strategy):
    params = (
        ('fast_ma', 10),
        ('slow_ma', 30),
        ('atr_period', 14),
        ('atr_multiplier_sl', 2.0),
        ('atr_multiplier_tp', 3.0),
        ('risk_percent', 2.0),
    )

    def __init__(self):
        # Indicators
        self.fast_ma = bt.indicators.SMA(self.data.close, period=self.p.fast_ma)
        self.slow_ma = bt.indicators.SMA(self.data.close, period=self.p.slow_ma)
        self.atr = bt.indicators.ATR(self.data, period=self.p.atr_period)
        self.crossover = bt.indicators.CrossOver(self.fast_ma, self.slow_ma)

        # Track orders
        self.order = None

    def next(self):
        if self.order:
            return  # Pending order

        if not self.position:
            # Entry logic
            if self.crossover > 0:
                # Calculate position size based on ATR risk
                risk_amount = self.broker.getvalue() * (self.p.risk_percent / 100)
                stop_distance = self.atr[0] * self.p.atr_multiplier_sl
                size = risk_amount / stop_distance

                # Place order with SL/TP
                stop_loss = self.data.close[0] - stop_distance
                take_profit = self.data.close[0] + (self.atr[0] * self.p.atr_multiplier_tp)

                self.order = self.buy(size=size)
                self.sell(size=size, exectype=bt.Order.Stop, price=stop_loss)
                self.sell(size=size, exectype=bt.Order.Limit, price=take_profit)

        else:
            # Exit logic
            if self.crossover < 0:
                self.close()

    def notify_order(self, order):
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.2f}')
            elif order.issell():
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.2f}')
        self.order = None

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}')


# ==================== BACKTESTING SETUP ====================
def run_backtest():
    # Create Cerebro engine
    cerebro = bt.Cerebro()

    # Add strategy
    cerebro.addstrategy(TrendFollowingStrategy,
                        fast_ma=10,
                        slow_ma=30,
                        risk_percent=2.0)

    # Load data
    data = bt.feeds.GenericCSVData(
        dataname='EURUSD_H4.csv',
        dtformat='%Y-%m-%d %H:%M:%S',
        datetime=0,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5,
        openinterest=-1
    )

    cerebro.adddata(data)

    # Broker settings
    cerebro.broker.setcash(10000.0)
    cerebro.broker.setcommission(commission=0.0001)  # 0.01% commission

    # Add analyzers
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe', riskfreerate=0.02)
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
    cerebro.addanalyzer(bt.analyzers.SQN, _name='sqn')  # System Quality Number

    # Print starting conditions
    print(f'Starting Portfolio Value: ${cerebro.broker.getvalue():.2f}')

    # Run backtest
    results = cerebro.run()
    strat = results[0]

    # Print results
    print(f'\nFinal Portfolio Value: ${cerebro.broker.getvalue():.2f}')

    # Performance metrics
    print('\n=== PERFORMANCE METRICS ===')
    print(f'Sharpe Ratio: {strat.analyzers.sharpe.get_analysis()["sharperatio"]:.2f}')
    print(f'Max Drawdown: {strat.analyzers.drawdown.get_analysis()["max"]["drawdown"]:.2f}%')
    print(f'Total Return: {strat.analyzers.returns.get_analysis()["rtot"]:.2%}')
    print(f'SQN: {strat.analyzers.sqn.get_analysis()["sqn"]:.2f}')

    # Trade statistics
    trade_analysis = strat.analyzers.trades.get_analysis()
    total_trades = trade_analysis.total.closed

    if total_trades > 0:
        print(f'\n=== TRADE STATISTICS ===')
        print(f'Total Trades: {total_trades}')
        print(f'Won: {trade_analysis.won.total} ({trade_analysis.won.total/total_trades:.1%})')
        print(f'Lost: {trade_analysis.lost.total} ({trade_analysis.lost.total/total_trades:.1%})')

        if trade_analysis.won.total > 0:
            print(f'Avg Win: ${trade_analysis.won.pnl.average:.2f}')
            print(f'Largest Win: ${trade_analysis.won.pnl.max:.2f}')

        if trade_analysis.lost.total > 0:
            print(f'Avg Loss: ${trade_analysis.lost.pnl.average:.2f}')
            print(f'Largest Loss: ${trade_analysis.lost.pnl.max:.2f}')

        # Profit factor
        gross_profit = trade_analysis.won.pnl.total if trade_analysis.won.total > 0 else 0
        gross_loss = abs(trade_analysis.lost.pnl.total) if trade_analysis.lost.total > 0 else 1
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else 0
        print(f'Profit Factor: {profit_factor:.2f}')

    # Plot results
    cerebro.plot(style='candlestick')


if __name__ == '__main__':
    run_backtest()
```

---

## 4. Parameter Optimization {#optimization}

### 🎯 Optimization Methods

**1. Grid Search (Exhaustive)**
```python
# Test all parameter combinations
cerebro.optstrategy(
    TrendFollowingStrategy,
    fast_ma=range(5, 20, 2),      # [5, 7, 9, 11, 13, 15, 17, 19]
    slow_ma=range(20, 50, 5),     # [20, 25, 30, 35, 40, 45]
)

# Total combinations: 8 × 6 = 48 backtests
```

**2. Walk-Forward Optimization** ⭐⭐⭐⭐⭐ (Best!)
```
Process:
1. In-sample period (IS): Optimize parameters (e.g., 2020-2021)
2. Out-of-sample period (OOS): Test with optimal params (e.g., 2022)
3. Roll forward: Repeat with new windows

Example:
IS: 2020-01 to 2021-12 → Optimal: fast_ma=10, slow_ma=30
OOS: 2022-01 to 2022-12 → Test performance

IS: 2021-01 to 2022-12 → Optimal: fast_ma=12, slow_ma=28
OOS: 2023-01 to 2023-12 → Test performance

✅ Prevents overfitting
✅ Simulates real-world adaptation
✅ More robust results
```

**3. Genetic Algorithms** (Advanced)
```python
from deap import base, creator, tools, algorithms
import random

# Define fitness (maximize Sharpe Ratio)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_fast_ma", random.randint, 5, 20)
toolbox.register("attr_slow_ma", random.randint, 20, 50)
toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.attr_fast_ma, toolbox.attr_slow_ma), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate_strategy(individual):
    fast_ma, slow_ma = individual
    # Run backtest with these parameters
    sharpe = run_backtest_return_sharpe(fast_ma, slow_ma)
    return (sharpe,)

toolbox.register("evaluate", evaluate_strategy)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=[5, 20], up=[20, 50], indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run genetic algorithm
population = toolbox.population(n=50)
algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=20, verbose=True)
```

---

### 🎯 Avoiding Overfitting

**Red Flags:**
```
❌ Too many parameters (>5)
❌ Extreme parameter values
❌ IS performance >> OOS performance
❌ Sharp equity curve changes in OOS
❌ Win rate > 80% (too good to be true)
❌ No losing months
```

**Best Practices:**
```
✅ Use out-of-sample testing
✅ Limit parameters (Occam's Razor)
✅ Test on multiple markets
✅ Test on multiple time periods
✅ Use walk-forward analysis
✅ Penalize complexity (AIC/BIC)
✅ Monte Carlo simulation
```

---

## 5. Performance Metrics {#performance-metrics}

### 🎯 Essential Metrics

**1. Sharpe Ratio** ⭐⭐⭐⭐⭐
```
Formula: (Return - Risk-Free Rate) / Volatility

Interpretation:
< 1.0: Poor
1.0 - 2.0: Good
2.0 - 3.0: Very Good
> 3.0: Excellent

✅ Most important risk-adjusted metric
✅ Annualized for comparison
```

**2. Max Drawdown** ⭐⭐⭐⭐⭐
```
Formula: (Trough - Peak) / Peak

Example:
Peak: $10,000
Trough: $7,000
Max DD: -30%

Acceptable Levels:
< 10%: Excellent
10-20%: Good
20-30%: Acceptable
> 30%: High risk

✅ Shows worst-case scenario
✅ Critical for position sizing
```

**3. Profit Factor** ⭐⭐⭐⭐
```
Formula: Gross Profit / Gross Loss

Interpretation:
< 1.0: Losing system
1.0 - 1.5: Marginal
1.5 - 2.0: Good
> 2.0: Excellent

Example:
Gross Profit: $10,000
Gross Loss: $5,000
Profit Factor: 2.0
```

**4. Win Rate** ⭐⭐⭐
```
Formula: Winning Trades / Total Trades

⚠️ Not the most important metric!

Context Matters:
- Mean reversion: 60-70% win rate expected
- Trend following: 30-50% win rate acceptable (large winners)

✅ Combine with avg win/loss for full picture
```

**5. Expectancy** ⭐⭐⭐⭐⭐
```
Formula: (Win Rate × Avg Win) - (Loss Rate × Avg Loss)

Example:
Win Rate: 40%
Avg Win: $500
Loss Rate: 60%
Avg Loss: $200
Expectancy: (0.4 × $500) - (0.6 × $200) = $80 per trade

✅ Tells you expected $ per trade
✅ Must be positive to be profitable
```

---

## 6. Walk-Forward Analysis {#walk-forward}

```python
def walk_forward_analysis(data, is_period_months=12, oos_period_months=3, step_months=3):
    """
    Perform walk-forward analysis

    is_period_months: In-sample optimization period
    oos_period_months: Out-of-sample testing period
    step_months: Roll forward step size
    """
    results = []
    start_date = data.index[0]
    end_date = data.index[-1]

    current_date = start_date

    while current_date + pd.DateOffset(months=is_period_months + oos_period_months) <= end_date:
        # In-sample period
        is_start = current_date
        is_end = current_date + pd.DateOffset(months=is_period_months)
        is_data = data[is_start:is_end]

        # Optimize parameters on in-sample data
        optimal_params = optimize_strategy(is_data)

        # Out-of-sample period
        oos_start = is_end
        oos_end = oos_start + pd.DateOffset(months=oos_period_months)
        oos_data = data[oos_start:oos_end]

        # Test with optimal parameters on out-of-sample data
        oos_results = backtest_strategy(oos_data, optimal_params)

        results.append({
            'is_start': is_start,
            'is_end': is_end,
            'oos_start': oos_start,
            'oos_end': oos_end,
            'optimal_params': optimal_params,
            'oos_sharpe': oos_results['sharpe'],
            'oos_return': oos_results['return'],
            'oos_max_dd': oos_results['max_drawdown']
        })

        # Roll forward
        current_date += pd.DateOffset(months=step_months)

    return pd.DataFrame(results)
```

---

## 7. Live Trading Deployment {#live-trading}

### 🎯 Deployment Checklist

```
✅ Backtest on 3+ years data
✅ Walk-forward optimization completed
✅ Paper trading 3+ months (profitable)
✅ Risk management tested
✅ Error handling implemented
✅ Monitoring dashboard ready
✅ Kill switch mechanism
✅ Broker API tested
✅ VPS configured (if needed)
✅ Emergency contact list
```

---

## 8. Risk Management Integration {#risk-management}

```python
def calculate_position_size(account_balance, risk_percent, entry_price, stop_loss_price):
    """
    Calculate position size based on risk

    Args:
        account_balance: Total account equity
        risk_percent: Risk per trade (e.g., 2.0 for 2%)
        entry_price: Entry price
        stop_loss_price: Stop loss price

    Returns:
        Position size in units
    """
    risk_amount = account_balance * (risk_percent / 100)
    risk_per_unit = abs(entry_price - stop_loss_price)
    position_size = risk_amount / risk_per_unit

    return position_size
```

---

## 9. Execution Algorithms {#execution}

**TWAP (Time-Weighted Average Price):**
```
Split order evenly over time period

Example: Buy 1000 shares over 1 hour
- 00:00: Buy 100 shares
- 00:06: Buy 100 shares
- ... (every 6 minutes)
- 00:54: Buy 100 shares

✅ Reduces market impact
✅ Simple to implement
```

**VWAP (Volume-Weighted Average Price):**
```
Split order based on expected volume pattern

✅ Better execution price
❌ More complex
```

---

## 10. Production Best Practices {#production}

```python
# Logging
import logging
logging.basicConfig(filename='trading.log', level=logging.INFO)

# Error handling
try:
    place_order()
except Exception as e:
    logging.error(f"Order failed: {e}")
    send_alert(f"URGENT: Order execution failed - {e}")

# Health checks
def check_system_health():
    checks = {
        'broker_connection': test_broker_connection(),
        'data_feed': test_data_feed(),
        'account_balance': get_account_balance() > MIN_BALANCE,
        'open_positions': len(get_positions()) < MAX_POSITIONS
    }
    return all(checks.values())
```

---

**Master algorithmic trading and build systematic, profitable trading systems!** 🚀
